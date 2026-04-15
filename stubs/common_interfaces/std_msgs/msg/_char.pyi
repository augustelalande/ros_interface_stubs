# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class Char:
    def __init__(self, *, data: str = ..., check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def data(self) -> str: ...
    @data.setter
    def data(self, value: str) -> None: ...
