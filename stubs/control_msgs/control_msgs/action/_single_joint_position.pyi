# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import builtin_interfaces.msg
import std_msgs.msg
import unique_identifier_msgs.msg

class SingleJointPosition_Goal:
    def __init__(
        self,
        *,
        position: float = ...,
        min_duration: builtin_interfaces.msg.Duration = ...,
        max_velocity: float = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def position(self) -> float: ...
    @position.setter
    def position(self, value: float) -> None: ...
    @property
    def min_duration(self) -> builtin_interfaces.msg.Duration: ...
    @min_duration.setter
    def min_duration(self, value: builtin_interfaces.msg.Duration) -> None: ...
    @property
    def max_velocity(self) -> float: ...
    @max_velocity.setter
    def max_velocity(self, value: float) -> None: ...

class SingleJointPosition_Result:
    def __init__(self) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class SingleJointPosition_Feedback:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        position: float = ...,
        velocity: float = ...,
        error: float = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def position(self) -> float: ...
    @position.setter
    def position(self, value: float) -> None: ...
    @property
    def velocity(self) -> float: ...
    @velocity.setter
    def velocity(self, value: float) -> None: ...
    @property
    def error(self) -> float: ...
    @error.setter
    def error(self, value: float) -> None: ...

class SingleJointPosition_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: SingleJointPosition_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> SingleJointPosition_Goal: ...
    @goal.setter
    def goal(self, value: SingleJointPosition_Goal) -> None: ...

class SingleJointPosition_SendGoal_Response:
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

class SingleJointPosition_SendGoal:
    Request: TypeAlias = SingleJointPosition_SendGoal_Request
    Response: TypeAlias = SingleJointPosition_SendGoal_Response

class SingleJointPosition_GetResult_Request:
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

class SingleJointPosition_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: SingleJointPosition_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> SingleJointPosition_Result: ...
    @result.setter
    def result(self, value: SingleJointPosition_Result) -> None: ...

class SingleJointPosition_GetResult:
    Request: TypeAlias = SingleJointPosition_GetResult_Request
    Response: TypeAlias = SingleJointPosition_GetResult_Response

class SingleJointPosition_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: SingleJointPosition_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> SingleJointPosition_Feedback: ...
    @feedback.setter
    def feedback(self, value: SingleJointPosition_Feedback) -> None: ...

class SingleJointPosition:
    Goal: TypeAlias = SingleJointPosition_Goal
    Result: TypeAlias = SingleJointPosition_Result
    Feedback: TypeAlias = SingleJointPosition_Feedback

    class Impl:
        SendGoalService: TypeAlias = SingleJointPosition_SendGoal
        GetResultService: TypeAlias = SingleJointPosition_GetResult
        FeedbackMessage: TypeAlias = SingleJointPosition_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
