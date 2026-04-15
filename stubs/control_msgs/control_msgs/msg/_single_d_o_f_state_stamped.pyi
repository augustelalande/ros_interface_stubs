# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg
import std_msgs.msg

class SingleDOFStateStamped:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        dof_state: control_msgs.msg.SingleDOFState = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def dof_state(self) -> control_msgs.msg.SingleDOFState: ...
    @dof_state.setter
    def dof_state(self, value: control_msgs.msg.SingleDOFState) -> None: ...
