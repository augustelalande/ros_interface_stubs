# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import builtin_interfaces.msg
import geometry_msgs.msg
import unique_identifier_msgs.msg

class PointHead_Goal:
    def __init__(
        self,
        *,
        target: geometry_msgs.msg.PointStamped = ...,
        pointing_axis: geometry_msgs.msg.Vector3 = ...,
        pointing_frame: str = ...,
        min_duration: builtin_interfaces.msg.Duration = ...,
        max_velocity: float = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def target(self) -> geometry_msgs.msg.PointStamped: ...
    @target.setter
    def target(self, value: geometry_msgs.msg.PointStamped) -> None: ...
    @property
    def pointing_axis(self) -> geometry_msgs.msg.Vector3: ...
    @pointing_axis.setter
    def pointing_axis(self, value: geometry_msgs.msg.Vector3) -> None: ...
    @property
    def pointing_frame(self) -> str: ...
    @pointing_frame.setter
    def pointing_frame(self, value: str) -> None: ...
    @property
    def min_duration(self) -> builtin_interfaces.msg.Duration: ...
    @min_duration.setter
    def min_duration(self, value: builtin_interfaces.msg.Duration) -> None: ...
    @property
    def max_velocity(self) -> float: ...
    @max_velocity.setter
    def max_velocity(self, value: float) -> None: ...

class PointHead_Result:
    def __init__(self) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class PointHead_Feedback:
    def __init__(
        self,
        *,
        pointing_angle_error: float = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def pointing_angle_error(self) -> float: ...
    @pointing_angle_error.setter
    def pointing_angle_error(self, value: float) -> None: ...

class PointHead_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: PointHead_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> PointHead_Goal: ...
    @goal.setter
    def goal(self, value: PointHead_Goal) -> None: ...

class PointHead_SendGoal_Response:
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

class PointHead_SendGoal:
    Request: TypeAlias = PointHead_SendGoal_Request
    Response: TypeAlias = PointHead_SendGoal_Response

class PointHead_GetResult_Request:
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

class PointHead_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: PointHead_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> PointHead_Result: ...
    @result.setter
    def result(self, value: PointHead_Result) -> None: ...

class PointHead_GetResult:
    Request: TypeAlias = PointHead_GetResult_Request
    Response: TypeAlias = PointHead_GetResult_Response

class PointHead_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: PointHead_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> PointHead_Feedback: ...
    @feedback.setter
    def feedback(self, value: PointHead_Feedback) -> None: ...

class PointHead:
    Goal: TypeAlias = PointHead_Goal
    Result: TypeAlias = PointHead_Result
    Feedback: TypeAlias = PointHead_Feedback

    class Impl:
        SendGoalService: TypeAlias = PointHead_SendGoal
        GetResultService: TypeAlias = PointHead_GetResult
        FeedbackMessage: TypeAlias = PointHead_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
