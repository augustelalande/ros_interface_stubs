# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import builtin_interfaces.msg
import control_msgs.msg
import std_msgs.msg
import unique_identifier_msgs.msg

class FollowJointWrenchTrajectory_Goal:
    def __init__(
        self,
        *,
        trajectory: control_msgs.msg.JointWrenchTrajectory = ...,
        path_tolerance: list[control_msgs.msg.JointTolerance] = ...,
        goal_tolerance: list[control_msgs.msg.JointTolerance] = ...,
        goal_time_tolerance: builtin_interfaces.msg.Duration = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def trajectory(self) -> control_msgs.msg.JointWrenchTrajectory: ...
    @trajectory.setter
    def trajectory(self, value: control_msgs.msg.JointWrenchTrajectory) -> None: ...
    @property
    def path_tolerance(self) -> list[control_msgs.msg.JointTolerance]: ...
    @path_tolerance.setter
    def path_tolerance(self, value: list[control_msgs.msg.JointTolerance]) -> None: ...
    @property
    def goal_tolerance(self) -> list[control_msgs.msg.JointTolerance]: ...
    @goal_tolerance.setter
    def goal_tolerance(self, value: list[control_msgs.msg.JointTolerance]) -> None: ...
    @property
    def goal_time_tolerance(self) -> builtin_interfaces.msg.Duration: ...
    @goal_time_tolerance.setter
    def goal_time_tolerance(self, value: builtin_interfaces.msg.Duration) -> None: ...

class FollowJointWrenchTrajectory_Result:
    # Constants

    SUCCESSFUL: int = 0

    INVALID_GOAL: int = -1

    INVALID_JOINTS: int = -2

    OLD_HEADER_TIMESTAMP: int = -3

    PATH_TOLERANCE_VIOLATED: int = -4

    GOAL_TOLERANCE_VIOLATED: int = -5

    TRAJECTORY_ABORTED: int = -6

    def __init__(
        self,
        *,
        error_code: int = ...,
        error_string: str = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def error_code(self) -> int: ...
    @error_code.setter
    def error_code(self, value: int) -> None: ...
    @property
    def error_string(self) -> str: ...
    @error_string.setter
    def error_string(self, value: str) -> None: ...

class FollowJointWrenchTrajectory_Feedback:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        joint_names: list[str] = ...,
        desired: control_msgs.msg.JointWrenchTrajectoryPoint = ...,
        actual: control_msgs.msg.JointWrenchTrajectoryPoint = ...,
        error: control_msgs.msg.JointWrenchTrajectoryPoint = ...,
        index: int = ...,
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
    def desired(self) -> control_msgs.msg.JointWrenchTrajectoryPoint: ...
    @desired.setter
    def desired(self, value: control_msgs.msg.JointWrenchTrajectoryPoint) -> None: ...
    @property
    def actual(self) -> control_msgs.msg.JointWrenchTrajectoryPoint: ...
    @actual.setter
    def actual(self, value: control_msgs.msg.JointWrenchTrajectoryPoint) -> None: ...
    @property
    def error(self) -> control_msgs.msg.JointWrenchTrajectoryPoint: ...
    @error.setter
    def error(self, value: control_msgs.msg.JointWrenchTrajectoryPoint) -> None: ...
    @property
    def index(self) -> int: ...
    @index.setter
    def index(self, value: int) -> None: ...

class FollowJointWrenchTrajectory_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: FollowJointWrenchTrajectory_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> FollowJointWrenchTrajectory_Goal: ...
    @goal.setter
    def goal(self, value: FollowJointWrenchTrajectory_Goal) -> None: ...

class FollowJointWrenchTrajectory_SendGoal_Response:
    def __init__(
        self,
        *,
        accepted: bool = ...,
        stamp: builtin_interfaces.msg.Time = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def accepted(self) -> bool: ...
    @accepted.setter
    def accepted(self, value: bool) -> None: ...
    @property
    def stamp(self) -> builtin_interfaces.msg.Time: ...
    @stamp.setter
    def stamp(self, value: builtin_interfaces.msg.Time) -> None: ...

class FollowJointWrenchTrajectory_SendGoal:
    Request: TypeAlias = FollowJointWrenchTrajectory_SendGoal_Request
    Response: TypeAlias = FollowJointWrenchTrajectory_SendGoal_Response

class FollowJointWrenchTrajectory_GetResult_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...

class FollowJointWrenchTrajectory_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: FollowJointWrenchTrajectory_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> FollowJointWrenchTrajectory_Result: ...
    @result.setter
    def result(self, value: FollowJointWrenchTrajectory_Result) -> None: ...

class FollowJointWrenchTrajectory_GetResult:
    Request: TypeAlias = FollowJointWrenchTrajectory_GetResult_Request
    Response: TypeAlias = FollowJointWrenchTrajectory_GetResult_Response

class FollowJointWrenchTrajectory_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: FollowJointWrenchTrajectory_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> FollowJointWrenchTrajectory_Feedback: ...
    @feedback.setter
    def feedback(self, value: FollowJointWrenchTrajectory_Feedback) -> None: ...

class FollowJointWrenchTrajectory:
    Goal: TypeAlias = FollowJointWrenchTrajectory_Goal
    Result: TypeAlias = FollowJointWrenchTrajectory_Result
    Feedback: TypeAlias = FollowJointWrenchTrajectory_Feedback

    class Impl:
        SendGoalService: TypeAlias = FollowJointWrenchTrajectory_SendGoal
        GetResultService: TypeAlias = FollowJointWrenchTrajectory_GetResult
        FeedbackMessage: TypeAlias = FollowJointWrenchTrajectory_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
