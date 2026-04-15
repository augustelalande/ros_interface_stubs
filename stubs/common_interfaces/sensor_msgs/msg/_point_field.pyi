# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class PointField:
    # Constants
    INT8: int = 1
    UINT8: int = 2
    INT16: int = 3
    UINT16: int = 4
    INT32: int = 5
    UINT32: int = 6
    FLOAT32: int = 7
    FLOAT64: int = 8
    INT64: int = 9
    UINT64: int = 10
    BOOL: int = 11

    def __init__(
        self,
        *,
        name: str = ...,
        offset: int = ...,
        datatype: int = ...,
        count: int = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def offset(self) -> int: ...
    @offset.setter
    def offset(self, value: int) -> None: ...
    @property
    def datatype(self) -> int: ...
    @datatype.setter
    def datatype(self, value: int) -> None: ...
    @property
    def count(self) -> int: ...
    @count.setter
    def count(self, value: int) -> None: ...
