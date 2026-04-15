# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg
import std_msgs.msg

class MultiDOFStateStamped:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        dof_states: list[control_msgs.msg.SingleDOFState] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def dof_states(self) -> list[control_msgs.msg.SingleDOFState]: ...
    @dof_states.setter
    def dof_states(self, value: list[control_msgs.msg.SingleDOFState]) -> None: ...
