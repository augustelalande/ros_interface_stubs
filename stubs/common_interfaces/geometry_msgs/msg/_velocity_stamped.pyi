# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class VelocityStamped:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        body_frame_id: str = ...,
        reference_frame_id: str = ...,
        velocity: geometry_msgs.msg.Twist = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def body_frame_id(self) -> str: ...
    @body_frame_id.setter
    def body_frame_id(self, value: str) -> None: ...
    @property
    def reference_frame_id(self) -> str: ...
    @reference_frame_id.setter
    def reference_frame_id(self, value: str) -> None: ...
    @property
    def velocity(self) -> geometry_msgs.msg.Twist: ...
    @velocity.setter
    def velocity(self, value: geometry_msgs.msg.Twist) -> None: ...
