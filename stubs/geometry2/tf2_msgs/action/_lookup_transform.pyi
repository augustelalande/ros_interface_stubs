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
import tf2_msgs.msg
import unique_identifier_msgs.msg

class LookupTransform_Goal:
    def __init__(
        self,
        *,
        target_frame: str = ...,
        source_frame: str = ...,
        source_time: builtin_interfaces.msg.Time = ...,
        timeout: builtin_interfaces.msg.Duration = ...,
        target_time: builtin_interfaces.msg.Time = ...,
        fixed_frame: str = ...,
        advanced: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def target_frame(self) -> str: ...
    @target_frame.setter
    def target_frame(self, value: str) -> None: ...
    @property
    def source_frame(self) -> str: ...
    @source_frame.setter
    def source_frame(self, value: str) -> None: ...
    @property
    def source_time(self) -> builtin_interfaces.msg.Time: ...
    @source_time.setter
    def source_time(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def timeout(self) -> builtin_interfaces.msg.Duration: ...
    @timeout.setter
    def timeout(self, value: builtin_interfaces.msg.Duration) -> None: ...
    @property
    def target_time(self) -> builtin_interfaces.msg.Time: ...
    @target_time.setter
    def target_time(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def fixed_frame(self) -> str: ...
    @fixed_frame.setter
    def fixed_frame(self, value: str) -> None: ...
    @property
    def advanced(self) -> bool: ...
    @advanced.setter
    def advanced(self, value: bool) -> None: ...

class LookupTransform_Result:
    def __init__(
        self,
        *,
        transform: geometry_msgs.msg.TransformStamped = ...,
        error: tf2_msgs.msg.TF2Error = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def transform(self) -> geometry_msgs.msg.TransformStamped: ...
    @transform.setter
    def transform(self, value: geometry_msgs.msg.TransformStamped) -> None: ...
    @property
    def error(self) -> tf2_msgs.msg.TF2Error: ...
    @error.setter
    def error(self, value: tf2_msgs.msg.TF2Error) -> None: ...

class LookupTransform_Feedback:
    def __init__(self) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class LookupTransform_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: LookupTransform_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> LookupTransform_Goal: ...
    @goal.setter
    def goal(self, value: LookupTransform_Goal) -> None: ...

class LookupTransform_SendGoal_Response:
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

class LookupTransform_SendGoal:
    Request: TypeAlias = LookupTransform_SendGoal_Request
    Response: TypeAlias = LookupTransform_SendGoal_Response

class LookupTransform_GetResult_Request:
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

class LookupTransform_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: LookupTransform_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> LookupTransform_Result: ...
    @result.setter
    def result(self, value: LookupTransform_Result) -> None: ...

class LookupTransform_GetResult:
    Request: TypeAlias = LookupTransform_GetResult_Request
    Response: TypeAlias = LookupTransform_GetResult_Response

class LookupTransform_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: LookupTransform_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> LookupTransform_Feedback: ...
    @feedback.setter
    def feedback(self, value: LookupTransform_Feedback) -> None: ...

class LookupTransform:
    Goal: TypeAlias = LookupTransform_Goal
    Result: TypeAlias = LookupTransform_Result
    Feedback: TypeAlias = LookupTransform_Feedback

    class Impl:
        SendGoalService: TypeAlias = LookupTransform_SendGoal
        GetResultService: TypeAlias = LookupTransform_GetResult
        FeedbackMessage: TypeAlias = LookupTransform_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
