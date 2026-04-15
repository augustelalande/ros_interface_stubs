# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class TrajectoryPoint:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        pose: geometry_msgs.msg.Pose = ...,
        velocity: geometry_msgs.msg.Twist = ...,
        acceleration: geometry_msgs.msg.Accel = ...,
        effort: geometry_msgs.msg.Wrench = ...,
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
    def pose(self) -> geometry_msgs.msg.Pose: ...
    @pose.setter
    def pose(self, value: geometry_msgs.msg.Pose) -> None: ...
    @property
    def velocity(self) -> geometry_msgs.msg.Twist: ...
    @velocity.setter
    def velocity(self, value: geometry_msgs.msg.Twist) -> None: ...
    @property
    def acceleration(self) -> geometry_msgs.msg.Accel: ...
    @acceleration.setter
    def acceleration(self, value: geometry_msgs.msg.Accel) -> None: ...
    @property
    def effort(self) -> geometry_msgs.msg.Wrench: ...
    @effort.setter
    def effort(self, value: geometry_msgs.msg.Wrench) -> None: ...
