# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg
import geometry_msgs.msg

class MotionPrimitive:
    # Constants
    UNKNOWN: int = -1
    LINEAR_JOINT: int = 0
    LINEAR_CARTESIAN: int = 50
    CIRCULAR_CARTESIAN: int = 51

    def __init__(
        self,
        *,
        type: int = ...,  # noqa: A002
        blend_radius: float = ...,
        additional_arguments: list[control_msgs.msg.MotionArgument] = ...,
        poses: list[geometry_msgs.msg.PoseStamped] = ...,
        joint_positions: list[float] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def type(self) -> int: ...
    @type.setter
    def type(self, value: int) -> None: ...
    @property
    def blend_radius(self) -> float: ...
    @blend_radius.setter
    def blend_radius(self, value: float) -> None: ...
    @property
    def additional_arguments(self) -> list[control_msgs.msg.MotionArgument]: ...
    @additional_arguments.setter
    def additional_arguments(
        self, value: list[control_msgs.msg.MotionArgument]
    ) -> None: ...
    @property
    def poses(self) -> list[geometry_msgs.msg.PoseStamped]: ...
    @poses.setter
    def poses(self, value: list[geometry_msgs.msg.PoseStamped]) -> None: ...
    @property
    def joint_positions(self) -> list[float]: ...
    @joint_positions.setter
    def joint_positions(self, value: list[float]) -> None: ...
