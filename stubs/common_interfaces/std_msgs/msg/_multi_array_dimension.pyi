# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class MultiArrayDimension:
    def __init__(
        self,
        *,
        label: str = ...,
        size: int = ...,
        stride: int = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str) -> None: ...
    @property
    def size(self) -> int: ...
    @size.setter
    def size(self, value: int) -> None: ...
    @property
    def stride(self) -> int: ...
    @stride.setter
    def stride(self, value: int) -> None: ...
