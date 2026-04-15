# ros_interface_stubs

Python stub files (`.pyi`) for common ROS 2 interfaces, so you can typecheck ROS 2 Python code without a ROS installation.

## Motivation

ROS 2 message, service, and action types are only available as Python modules inside a sourced ROS environment. This makes it impossible to run a type checker such as Pyright or mypy on ROS 2 Python code in a standard CI environment or on a developer machine that doesn't have ROS installed.

This project generates `.pyi` stub files from the raw `.msg`, `.srv`, and `.action` interface definitions, covering the most common ROS 2 interface packages:

| Package group | Packages |
|---|---|
| `common_interfaces` | `diagnostic_msgs`, `geometry_msgs`, `nav_msgs`, `sensor_msgs`, `shape_msgs`, `std_msgs`, `std_srvs`, `stereo_msgs`, `trajectory_msgs`, `visualization_msgs` |
| `rcl_interfaces` | `action_msgs`, `builtin_interfaces`, `composition_interfaces`, `lifecycle_msgs`, `rcl_interfaces`, `rosgraph_msgs`, `statistics_msgs`, `type_description_interfaces` |
| `unique_identifier_msgs` | `unique_identifier_msgs` |

## Usage

Copy the package directories you need from `stubs/` into your project.

```
your_project/
  stubs/
    common_interfaces/     # copied from this repo
      geometry_msgs/
      std_msgs/
      ...
  src/
    your_ros_node.py
```

Then tell your type checker where to find them.

### Pyright

```toml
# pyproject.toml
[tool.pyright]
extraPaths = ["stubs/common_interfaces"]
```

### mypy

```ini
# mypy.ini
[mypy]
mypy_path = stubs/common_interfaces
```

## Generating stubs for other packages

The generator works on any ROS 2 interface package, not just the ones included here. To generate stubs for additional packages, place the package folder under `interfaces/` and re-run the script:

```
interfaces/
  my_custom_msgs/        # added package (contains msg/, srv/, and/or action/)
  my_group/              # or nested under a group folder
    my_other_msgs/
```

```bash
uv run python scripts/generate_stubs.py
```

The generated stubs will appear under `stubs/` following the same structure, ready to copy into your project.

## Regenerating stubs

The stubs are generated from the interface definitions under `interfaces/`. To regenerate them after updating the interface submodules:

```bash
uv run python scripts/generate_stubs.py
```

This requires [uv](https://docs.astral.sh/uv/). The script depends on `jinja2` and `ruff` (declared in `pyproject.toml`).

## Project structure

```
interfaces/          # ROS 2 interface definitions (git submodules)
  common_interfaces/
  rcl_interfaces/
  unique_identifier_msgs/
scripts/
  generate_stubs.py  # stub generator
  templates/         # Jinja2 templates for .pyi files
stubs/               # generated output — checked in for direct use
  common_interfaces/
  rcl_interfaces/
  unique_identifier_msgs/
```

## Type mapping

ROS primitive types map to Python types as follows:

| ROS type | Python type |
|---|---|
| `bool` | `bool` |
| `byte` | `bytes` (fields) / `int` (constants) |
| `char` | `str` |
| `float32`, `float64` | `float` |
| `int8` … `uint64` | `int` |
| `string`, `wstring` | `str` |
| `string<=N` | `str` (bounded string) |
| `T[]` | `list[T]` (unbounded array) |
| `T[N]` | `list[T]` (static array) |
| `T[<=N]` | `list[T]` (bounded array) |
| `pkg/Msg` | `pkg.msg.Msg` |
