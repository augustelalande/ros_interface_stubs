# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class Float64Values:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        values: list[float] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def values(self) -> list[float]: ...
    @values.setter
    def values(self, value: list[float]) -> None: ...
