# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class MecanumDriveControllerState:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        front_left_wheel_velocity: float = ...,
        back_left_wheel_velocity: float = ...,
        back_right_wheel_velocity: float = ...,
        front_right_wheel_velocity: float = ...,
        reference_velocity: geometry_msgs.msg.Twist = ...,
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
    def front_left_wheel_velocity(self) -> float: ...
    @front_left_wheel_velocity.setter
    def front_left_wheel_velocity(self, value: float) -> None: ...
    @property
    def back_left_wheel_velocity(self) -> float: ...
    @back_left_wheel_velocity.setter
    def back_left_wheel_velocity(self, value: float) -> None: ...
    @property
    def back_right_wheel_velocity(self) -> float: ...
    @back_right_wheel_velocity.setter
    def back_right_wheel_velocity(self, value: float) -> None: ...
    @property
    def front_right_wheel_velocity(self) -> float: ...
    @front_right_wheel_velocity.setter
    def front_right_wheel_velocity(self, value: float) -> None: ...
    @property
    def reference_velocity(self) -> geometry_msgs.msg.Twist: ...
    @reference_velocity.setter
    def reference_velocity(self, value: geometry_msgs.msg.Twist) -> None: ...
