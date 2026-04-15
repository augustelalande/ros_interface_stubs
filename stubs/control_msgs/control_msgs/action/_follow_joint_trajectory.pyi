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
import trajectory_msgs.msg
import unique_identifier_msgs.msg

class FollowJointTrajectory_Goal:
    def __init__(
        self,
        *,
        trajectory: trajectory_msgs.msg.JointTrajectory = ...,
        multi_dof_trajectory: trajectory_msgs.msg.MultiDOFJointTrajectory = ...,
        path_tolerance: list[control_msgs.msg.JointTolerance] = ...,
        component_path_tolerance: list[control_msgs.msg.JointComponentTolerance] = ...,
        goal_tolerance: list[control_msgs.msg.JointTolerance] = ...,
        component_goal_tolerance: list[control_msgs.msg.JointComponentTolerance] = ...,
        goal_time_tolerance: builtin_interfaces.msg.Duration = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def trajectory(self) -> trajectory_msgs.msg.JointTrajectory: ...
    @trajectory.setter
    def trajectory(self, value: trajectory_msgs.msg.JointTrajectory) -> None: ...
    @property
    def multi_dof_trajectory(self) -> trajectory_msgs.msg.MultiDOFJointTrajectory: ...
    @multi_dof_trajectory.setter
    def multi_dof_trajectory(
        self, value: trajectory_msgs.msg.MultiDOFJointTrajectory
    ) -> None: ...
    @property
    def path_tolerance(self) -> list[control_msgs.msg.JointTolerance]: ...
    @path_tolerance.setter
    def path_tolerance(self, value: list[control_msgs.msg.JointTolerance]) -> None: ...
    @property
    def component_path_tolerance(
        self,
    ) -> list[control_msgs.msg.JointComponentTolerance]: ...
    @component_path_tolerance.setter
    def component_path_tolerance(
        self, value: list[control_msgs.msg.JointComponentTolerance]
    ) -> None: ...
    @property
    def goal_tolerance(self) -> list[control_msgs.msg.JointTolerance]: ...
    @goal_tolerance.setter
    def goal_tolerance(self, value: list[control_msgs.msg.JointTolerance]) -> None: ...
    @property
    def component_goal_tolerance(
        self,
    ) -> list[control_msgs.msg.JointComponentTolerance]: ...
    @component_goal_tolerance.setter
    def component_goal_tolerance(
        self, value: list[control_msgs.msg.JointComponentTolerance]
    ) -> None: ...
    @property
    def goal_time_tolerance(self) -> builtin_interfaces.msg.Duration: ...
    @goal_time_tolerance.setter
    def goal_time_tolerance(self, value: builtin_interfaces.msg.Duration) -> None: ...

class FollowJointTrajectory_Result:
    # Constants

    SUCCESSFUL: int = 0

    INVALID_GOAL: int = -1

    INVALID_JOINTS: int = -2

    OLD_HEADER_TIMESTAMP: int = -3

    PATH_TOLERANCE_VIOLATED: int = -4

    GOAL_TOLERANCE_VIOLATED: int = -5

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

class FollowJointTrajectory_Feedback:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        joint_names: list[str] = ...,
        desired: trajectory_msgs.msg.JointTrajectoryPoint = ...,
        actual: trajectory_msgs.msg.JointTrajectoryPoint = ...,
        error: trajectory_msgs.msg.JointTrajectoryPoint = ...,
        index: int = ...,
        multi_dof_joint_names: list[str] = ...,
        multi_dof_desired: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint = ...,
        multi_dof_actual: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint = ...,
        multi_dof_error: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint = ...,
        multi_dof_index: int = ...,
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
    def desired(self) -> trajectory_msgs.msg.JointTrajectoryPoint: ...
    @desired.setter
    def desired(self, value: trajectory_msgs.msg.JointTrajectoryPoint) -> None: ...
    @property
    def actual(self) -> trajectory_msgs.msg.JointTrajectoryPoint: ...
    @actual.setter
    def actual(self, value: trajectory_msgs.msg.JointTrajectoryPoint) -> None: ...
    @property
    def error(self) -> trajectory_msgs.msg.JointTrajectoryPoint: ...
    @error.setter
    def error(self, value: trajectory_msgs.msg.JointTrajectoryPoint) -> None: ...
    @property
    def index(self) -> int: ...
    @index.setter
    def index(self, value: int) -> None: ...
    @property
    def multi_dof_joint_names(self) -> list[str]: ...
    @multi_dof_joint_names.setter
    def multi_dof_joint_names(self, value: list[str]) -> None: ...
    @property
    def multi_dof_desired(self) -> trajectory_msgs.msg.MultiDOFJointTrajectoryPoint: ...
    @multi_dof_desired.setter
    def multi_dof_desired(
        self, value: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint
    ) -> None: ...
    @property
    def multi_dof_actual(self) -> trajectory_msgs.msg.MultiDOFJointTrajectoryPoint: ...
    @multi_dof_actual.setter
    def multi_dof_actual(
        self, value: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint
    ) -> None: ...
    @property
    def multi_dof_error(self) -> trajectory_msgs.msg.MultiDOFJointTrajectoryPoint: ...
    @multi_dof_error.setter
    def multi_dof_error(
        self, value: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint
    ) -> None: ...
    @property
    def multi_dof_index(self) -> int: ...
    @multi_dof_index.setter
    def multi_dof_index(self, value: int) -> None: ...

class FollowJointTrajectory_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: FollowJointTrajectory_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> FollowJointTrajectory_Goal: ...
    @goal.setter
    def goal(self, value: FollowJointTrajectory_Goal) -> None: ...

class FollowJointTrajectory_SendGoal_Response:
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

class FollowJointTrajectory_SendGoal:
    Request: TypeAlias = FollowJointTrajectory_SendGoal_Request
    Response: TypeAlias = FollowJointTrajectory_SendGoal_Response

class FollowJointTrajectory_GetResult_Request:
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

class FollowJointTrajectory_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: FollowJointTrajectory_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> FollowJointTrajectory_Result: ...
    @result.setter
    def result(self, value: FollowJointTrajectory_Result) -> None: ...

class FollowJointTrajectory_GetResult:
    Request: TypeAlias = FollowJointTrajectory_GetResult_Request
    Response: TypeAlias = FollowJointTrajectory_GetResult_Response

class FollowJointTrajectory_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: FollowJointTrajectory_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> FollowJointTrajectory_Feedback: ...
    @feedback.setter
    def feedback(self, value: FollowJointTrajectory_Feedback) -> None: ...

class FollowJointTrajectory:
    Goal: TypeAlias = FollowJointTrajectory_Goal
    Result: TypeAlias = FollowJointTrajectory_Result
    Feedback: TypeAlias = FollowJointTrajectory_Feedback

    class Impl:
        SendGoalService: TypeAlias = FollowJointTrajectory_SendGoal
        GetResultService: TypeAlias = FollowJointTrajectory_GetResult
        FeedbackMessage: TypeAlias = FollowJointTrajectory_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
