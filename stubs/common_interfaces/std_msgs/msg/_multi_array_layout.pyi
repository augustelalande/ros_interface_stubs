# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class MultiArrayLayout:
    def __init__(
        self,
        *,
        dim: list[std_msgs.msg.MultiArrayDimension] = ...,
        data_offset: int = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def dim(self) -> list[std_msgs.msg.MultiArrayDimension]: ...
    @dim.setter
    def dim(self, value: list[std_msgs.msg.MultiArrayDimension]) -> None: ...
    @property
    def data_offset(self) -> int: ...
    @data_offset.setter
    def data_offset(self, value: int) -> None: ...
