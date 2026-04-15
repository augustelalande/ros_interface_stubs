# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg
import std_msgs.msg

class DynamicInterfaceGroupValues:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        interface_groups: list[str] = ...,
        interface_values: list[control_msgs.msg.InterfaceValue] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def interface_groups(self) -> list[str]: ...
    @interface_groups.setter
    def interface_groups(self, value: list[str]) -> None: ...
    @property
    def interface_values(self) -> list[control_msgs.msg.InterfaceValue]: ...
    @interface_values.setter
    def interface_values(
        self, value: list[control_msgs.msg.InterfaceValue]
    ) -> None: ...
