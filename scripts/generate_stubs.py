from __future__ import annotations

import re
import shutil
import subprocess  # noqa: S404
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

FILE_DIR = Path(__file__).parent
TEMPLATES_PATH = FILE_DIR / "templates"
INTERFACES_DIR = FILE_DIR.parent / "interfaces"
OUT_DIR = FILE_DIR.parent / "stubs"

JINJA_ENV = Environment(loader=FileSystemLoader(TEMPLATES_PATH), autoescape=True)
JINJA_ENV.globals.update(builtins=set(dir(__builtins__)))
JINJA_ENV.globals.update(zip=zip)

ROS_TO_PYTHON = {
    "bool": "bool",
    "byte": "bytes",
    "char": "str",
    "float32": "float",
    "float64": "float",
    "int8": "int",
    "uint8": "int",
    "int16": "int",
    "uint16": "int",
    "int32": "int",
    "uint32": "int",
    "int64": "int",
    "uint64": "int",
    "string": "str",
    "wstring": "str",
}


def title_to_snake(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z]+)", "_", name).lower()


def generate_message_file(
    name: str,
    fields: dict[str, str],
    constants: dict[str, tuple[str, str]],
    imports: list[str],
) -> str:
    template = JINJA_ENV.get_template("message.j2")
    return template.render(
        name=name, fields=fields, constants=constants, imports=imports
    )


def generate_service_file(
    name: str,
    request_fields: dict[str, str],
    request_constants: dict[str, tuple[str, str]],
    response_fields: dict[str, str],
    response_constants: dict[str, tuple[str, str]],
    imports: list[str],
) -> str:
    template = JINJA_ENV.get_template("service.j2")
    return template.render(
        name=name,
        request_fields=request_fields,
        request_constants=request_constants,
        response_fields=response_fields,
        response_constants=response_constants,
        imports=imports,
    )


def generate_action_file(
    name: str,
    goal_fields: dict[str, str],
    goal_constants: dict[str, tuple[str, str]],
    result_fields: dict[str, str],
    result_constants: dict[str, tuple[str, str]],
    feedback_fields: dict[str, str],
    feedback_constants: dict[str, tuple[str, str]],
    imports: list[str],
) -> str:
    template = JINJA_ENV.get_template("action.j2")
    return template.render(
        name=name,
        goal_fields=goal_fields,
        goal_constants=goal_constants,
        result_fields=result_fields,
        result_constants=result_constants,
        feedback_fields=feedback_fields,
        feedback_constants=feedback_constants,
        imports=imports,
    )


def generate_init_file(clss: list[str], files: list[str]) -> str:
    template = JINJA_ENV.get_template("init.j2")
    return template.render(clss=clss, files=files)


def extract_python_type(
    _type: str, package: str, package_msgs: set[str]
) -> tuple[str, list[str]]:
    array_match = re.search(r"\[.*?\]$", _type)
    if array_match:
        base_type = _type[: array_match.start()]
        subtype, imports = extract_python_type(base_type, package, package_msgs)
        return f"list[{subtype}]", imports

    if re.fullmatch(r"string<=\d+", _type):
        return "str", []

    if _type in ROS_TO_PYTHON:
        return ROS_TO_PYTHON[_type], []

    if _type in package_msgs:
        return f"{package}.msg.{_type}", [f"import {package}.msg"]

    other_package, msg = _type.split("/")
    return f"{other_package}.msg.{msg}", [f"import {other_package}.msg"]


def extract_fields(
    section: str,
    package: str,
    package_msgs: set[str],
) -> tuple[dict[str, str], dict[str, tuple[str, str]], set[str]]:
    variable_fields: dict[str, str] = {}
    constant_fields: dict[str, tuple[str, str]] = {}
    imports: set[str] = set()

    for _line in section.split("\n"):
        line = _line.split("#")[0].strip()
        if not line:
            continue

        _type, rest = line.split(None, 1)
        python_type, new_imports = extract_python_type(_type, package, package_msgs)
        imports.update(new_imports)

        if "=" in rest:
            field_name, raw_value = rest.split("=", 1)
            # byte constants are integer literals in .msg files; bytes is not assignable from int
            if python_type == "bytes":
                python_type = "int"
            constant_fields[field_name.strip()] = (python_type, raw_value.strip())
        else:
            field_name = rest.split()[0]
            variable_fields[field_name] = python_type

    return variable_fields, constant_fields, imports


def generate_message_files(
    msg_files: list[Path], out_dir: Path, package: str, package_msgs: set[str]
) -> None:
    msg_out = out_dir / "msg"
    msg_out.mkdir(exist_ok=True)
    clss = []
    files = []

    for msg in msg_files:
        name = msg.stem
        filename = f"_{title_to_snake(name)}"
        clss.append(name)
        files.append(filename)
        variable_fields, constant_fields, imports = extract_fields(
            msg.read_text(encoding="utf-8"), package, package_msgs
        )
        out = generate_message_file(
            name, variable_fields, constant_fields, sorted(imports)
        )
        out_path = msg_out / f"{filename}.pyi"
        out_path.write_text(out)

    out = generate_init_file(clss, files)
    out_path = msg_out / "__init__.pyi"
    out_path.write_text(out)


def generate_service_files(
    srv_files: list[Path], out_dir: Path, package: str, package_msgs: set[str]
) -> None:
    srv_out = out_dir / "srv"
    srv_out.mkdir(exist_ok=True)
    clss = []
    files = []

    for srv in srv_files:
        name = srv.stem
        sections = srv.read_text(encoding="utf-8")
        filename = f"_{title_to_snake(name)}"
        clss.append(name)
        files.append(filename)

        request_section, response_section = sections.split("---")
        request_variable_fields, request_constant_fields, request_imports = (
            extract_fields(request_section, package, package_msgs)
        )
        response_variable_fields, response_constant_fields, response_imports = (
            extract_fields(response_section, package, package_msgs)
        )
        imports = set()
        imports.update(request_imports)
        imports.update(response_imports)

        out = generate_service_file(
            name,
            request_variable_fields,
            request_constant_fields,
            response_variable_fields,
            response_constant_fields,
            sorted(imports),
        )
        out_path = srv_out / f"{filename}.pyi"
        out_path.write_text(out)

    out = generate_init_file(clss, files)
    out_path = srv_out / "__init__.pyi"
    out_path.write_text(out)


def generate_action_files(
    action_files: list[Path], out_dir: Path, package: str, package_msgs: set[str]
) -> None:
    action_out = out_dir / "action"
    action_out.mkdir(exist_ok=True)
    clss = []
    files = []

    for action in action_files:
        name = action.stem
        sections = action.read_text(encoding="utf-8")
        filename = f"_{title_to_snake(name)}"
        clss.append(name)
        files.append(filename)

        goal_section, result_section, feedback_section = sections.split("---")
        goal_variable_fields, goal_constant_fields, goal_imports = extract_fields(
            goal_section, package, package_msgs
        )
        result_variable_fields, result_constant_fields, result_imports = extract_fields(
            result_section, package, package_msgs
        )
        feedback_variable_fields, feedback_constant_fields, feedback_imports = (
            extract_fields(feedback_section, package, package_msgs)
        )
        imports = set()
        imports.update(goal_imports)
        imports.update(result_imports)
        imports.update(feedback_imports)

        out = generate_action_file(
            name,
            goal_variable_fields,
            goal_constant_fields,
            result_variable_fields,
            result_constant_fields,
            feedback_variable_fields,
            feedback_constant_fields,
            sorted(imports),
        )
        out_path = action_out / f"{filename}.pyi"
        out_path.write_text(out)

    out = generate_init_file(clss, files)
    out_path = action_out / "__init__.pyi"
    out_path.write_text(out)


def generate_stubs_for_package(package_path: Path) -> None:
    package = package_path.name

    msg_files = list(package_path.glob("msg/*.msg"))
    srv_files = list(package_path.glob("srv/*.srv"))
    action_files = list(package_path.glob("action/*.action"))

    package_msgs = {f.stem for f in msg_files}
    if package_path.parent == INTERFACES_DIR:
        out_dir = OUT_DIR / package
    else:
        out_dir = OUT_DIR / package_path.parent.name / package
    out_dir.mkdir(parents=True, exist_ok=True)

    if msg_files:
        generate_message_files(msg_files, out_dir, package, package_msgs)
    if srv_files:
        generate_service_files(srv_files, out_dir, package, package_msgs)
    if action_files:
        generate_action_files(action_files, out_dir, package, package_msgs)


def generate_stubs() -> None:
    seen: set[Path] = set()
    for ext in ("*.msg", "*.srv", "*.action"):
        for path in INTERFACES_DIR.rglob(ext):
            package_path = path.parent.parent
            if package_path not in seen:
                seen.add(package_path)
                generate_stubs_for_package(package_path)


if __name__ == "__main__":
    shutil.rmtree(OUT_DIR, ignore_errors=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    generate_stubs()
    subprocess.run(  # noqa: S603
        ["ruff", "check", "--select", "I,RUF022", "--fix", str(OUT_DIR)],  # noqa: S607
        check=True,
    )
    subprocess.run(["ruff", "format", str(OUT_DIR)], check=True)  # noqa: S603, S607
