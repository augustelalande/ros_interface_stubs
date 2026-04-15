# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg
import std_msgs.msg

class DynamicJointState:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        joint_names: list[str] = ...,
        interface_values: list[control_msgs.msg.InterfaceValue] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def joint_names(self) -> list[str]: ...
    @joint_names.setter
    def joint_names(self, value: list[str]) -> None: ...
    @property
    def interface_values(self) -> list[control_msgs.msg.InterfaceValue]: ...
    @interface_values.setter
    def interface_values(
        self, value: list[control_msgs.msg.InterfaceValue]
    ) -> None: ...
