# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg
import std_msgs.msg

class DynamicInterfaceValues:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        states: control_msgs.msg.InterfaceValue = ...,
        commands: control_msgs.msg.InterfaceValue = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def states(self) -> control_msgs.msg.InterfaceValue: ...
    @states.setter
    def states(self, value: control_msgs.msg.InterfaceValue) -> None: ...
    @property
    def commands(self) -> control_msgs.msg.InterfaceValue: ...
    @commands.setter
    def commands(self, value: control_msgs.msg.InterfaceValue) -> None: ...
