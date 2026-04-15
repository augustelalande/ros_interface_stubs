# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg
import trajectory_msgs.msg

class MultiDOFJointTrajectory:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        joint_names: list[str] = ...,
        points: list[trajectory_msgs.msg.MultiDOFJointTrajectoryPoint] = ...,
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
    def points(self) -> list[trajectory_msgs.msg.MultiDOFJointTrajectoryPoint]: ...
    @points.setter
    def points(
        self, value: list[trajectory_msgs.msg.MultiDOFJointTrajectoryPoint]
    ) -> None: ...
