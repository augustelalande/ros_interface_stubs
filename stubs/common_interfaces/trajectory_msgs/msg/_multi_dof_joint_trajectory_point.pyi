# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg
import geometry_msgs.msg

class MultiDOFJointTrajectoryPoint:
    def __init__(
        self,
        *,
        transforms: list[geometry_msgs.msg.Transform] = ...,
        velocities: list[geometry_msgs.msg.Twist] = ...,
        accelerations: list[geometry_msgs.msg.Twist] = ...,
        time_from_start: builtin_interfaces.msg.Duration = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def transforms(self) -> list[geometry_msgs.msg.Transform]: ...
    @transforms.setter
    def transforms(self, value: list[geometry_msgs.msg.Transform]) -> None: ...
    @property
    def velocities(self) -> list[geometry_msgs.msg.Twist]: ...
    @velocities.setter
    def velocities(self, value: list[geometry_msgs.msg.Twist]) -> None: ...
    @property
    def accelerations(self) -> list[geometry_msgs.msg.Twist]: ...
    @accelerations.setter
    def accelerations(self, value: list[geometry_msgs.msg.Twist]) -> None: ...
    @property
    def time_from_start(self) -> builtin_interfaces.msg.Duration: ...
    @time_from_start.setter
    def time_from_start(self, value: builtin_interfaces.msg.Duration) -> None: ...
