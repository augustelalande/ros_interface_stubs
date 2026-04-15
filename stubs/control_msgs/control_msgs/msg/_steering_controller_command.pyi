# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class SteeringControllerCommand:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        steering_angle: float = ...,
        linear_velocity: float = ...,
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
    def steering_angle(self) -> float: ...
    @steering_angle.setter
    def steering_angle(self, value: float) -> None: ...
    @property
    def linear_velocity(self) -> float: ...
    @linear_velocity.setter
    def linear_velocity(self, value: float) -> None: ...
