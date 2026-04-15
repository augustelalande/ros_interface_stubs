# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class UUID:
    def __init__(self, *, uuid: list[int] = ..., check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def uuid(self) -> list[int]: ...
    @uuid.setter
    def uuid(self, value: list[int]) -> None: ...
