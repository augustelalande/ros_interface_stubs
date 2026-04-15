# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class TypeSource:
    def __init__(
        self,
        *,
        type_name: str = ...,
        encoding: str = ...,
        raw_file_contents: str = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def type_name(self) -> str: ...
    @type_name.setter
    def type_name(self, value: str) -> None: ...
    @property
    def encoding(self) -> str: ...
    @encoding.setter
    def encoding(self, value: str) -> None: ...
    @property
    def raw_file_contents(self) -> str: ...
    @raw_file_contents.setter
    def raw_file_contents(self, value: str) -> None: ...
