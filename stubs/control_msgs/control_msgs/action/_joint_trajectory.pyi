# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import builtin_interfaces.msg
import trajectory_msgs.msg
import unique_identifier_msgs.msg

class JointTrajectory_Goal:
    def __init__(
        self,
        *,
        trajectory: trajectory_msgs.msg.JointTrajectory = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def trajectory(self) -> trajectory_msgs.msg.JointTrajectory: ...
    @trajectory.setter
    def trajectory(self, value: trajectory_msgs.msg.JointTrajectory) -> None: ...

class JointTrajectory_Result:
    def __init__(self) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class JointTrajectory_Feedback:
    def __init__(self) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class JointTrajectory_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: JointTrajectory_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> JointTrajectory_Goal: ...
    @goal.setter
    def goal(self, value: JointTrajectory_Goal) -> None: ...

class JointTrajectory_SendGoal_Response:
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

class JointTrajectory_SendGoal:
    Request: TypeAlias = JointTrajectory_SendGoal_Request
    Response: TypeAlias = JointTrajectory_SendGoal_Response

class JointTrajectory_GetResult_Request:
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

class JointTrajectory_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: JointTrajectory_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> JointTrajectory_Result: ...
    @result.setter
    def result(self, value: JointTrajectory_Result) -> None: ...

class JointTrajectory_GetResult:
    Request: TypeAlias = JointTrajectory_GetResult_Request
    Response: TypeAlias = JointTrajectory_GetResult_Response

class JointTrajectory_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: JointTrajectory_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> JointTrajectory_Feedback: ...
    @feedback.setter
    def feedback(self, value: JointTrajectory_Feedback) -> None: ...

class JointTrajectory:
    Goal: TypeAlias = JointTrajectory_Goal
    Result: TypeAlias = JointTrajectory_Result
    Feedback: TypeAlias = JointTrajectory_Feedback

    class Impl:
        SendGoalService: TypeAlias = JointTrajectory_SendGoal
        GetResultService: TypeAlias = JointTrajectory_GetResult
        FeedbackMessage: TypeAlias = JointTrajectory_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
