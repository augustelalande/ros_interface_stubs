# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class TypeHash:
    def __init__(
        self,
        *,
        version: int = ...,
        value: list[int] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def version(self) -> int: ...
    @version.setter
    def version(self, value: int) -> None: ...
    @property
    def value(self) -> list[int]: ...
    @value.setter
    def value(self, value: list[int]) -> None: ...
