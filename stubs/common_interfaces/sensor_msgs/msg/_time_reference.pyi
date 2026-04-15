# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg
import std_msgs.msg

class TimeReference:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        time_ref: builtin_interfaces.msg.Time = ...,
        source: str = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def time_ref(self) -> builtin_interfaces.msg.Time: ...
    @time_ref.setter
    def time_ref(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def source(self) -> str: ...
    @source.setter
    def source(self, value: str) -> None: ...
