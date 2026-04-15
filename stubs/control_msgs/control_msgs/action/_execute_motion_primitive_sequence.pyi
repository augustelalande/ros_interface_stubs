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
import unique_identifier_msgs.msg

class ExecuteMotionPrimitiveSequence_Goal:
    def __init__(
        self,
        *,
        trajectory: control_msgs.msg.MotionPrimitiveSequence = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def trajectory(self) -> control_msgs.msg.MotionPrimitiveSequence: ...
    @trajectory.setter
    def trajectory(self, value: control_msgs.msg.MotionPrimitiveSequence) -> None: ...

class ExecuteMotionPrimitiveSequence_Result:
    # Constants

    SUCCESSFUL: int = 0

    INVALID_GOAL: int = -1

    OLD_HEADER_TIMESTAMP: int = -3

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

class ExecuteMotionPrimitiveSequence_Feedback:
    def __init__(
        self,
        *,
        current_primitive_index: int = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def current_primitive_index(self) -> int: ...
    @current_primitive_index.setter
    def current_primitive_index(self, value: int) -> None: ...

class ExecuteMotionPrimitiveSequence_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: ExecuteMotionPrimitiveSequence_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> ExecuteMotionPrimitiveSequence_Goal: ...
    @goal.setter
    def goal(self, value: ExecuteMotionPrimitiveSequence_Goal) -> None: ...

class ExecuteMotionPrimitiveSequence_SendGoal_Response:
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

class ExecuteMotionPrimitiveSequence_SendGoal:
    Request: TypeAlias = ExecuteMotionPrimitiveSequence_SendGoal_Request
    Response: TypeAlias = ExecuteMotionPrimitiveSequence_SendGoal_Response

class ExecuteMotionPrimitiveSequence_GetResult_Request:
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

class ExecuteMotionPrimitiveSequence_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: ExecuteMotionPrimitiveSequence_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> ExecuteMotionPrimitiveSequence_Result: ...
    @result.setter
    def result(self, value: ExecuteMotionPrimitiveSequence_Result) -> None: ...

class ExecuteMotionPrimitiveSequence_GetResult:
    Request: TypeAlias = ExecuteMotionPrimitiveSequence_GetResult_Request
    Response: TypeAlias = ExecuteMotionPrimitiveSequence_GetResult_Response

class ExecuteMotionPrimitiveSequence_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: ExecuteMotionPrimitiveSequence_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> ExecuteMotionPrimitiveSequence_Feedback: ...
    @feedback.setter
    def feedback(self, value: ExecuteMotionPrimitiveSequence_Feedback) -> None: ...

class ExecuteMotionPrimitiveSequence:
    Goal: TypeAlias = ExecuteMotionPrimitiveSequence_Goal
    Result: TypeAlias = ExecuteMotionPrimitiveSequence_Result
    Feedback: TypeAlias = ExecuteMotionPrimitiveSequence_Feedback

    class Impl:
        SendGoalService: TypeAlias = ExecuteMotionPrimitiveSequence_SendGoal
        GetResultService: TypeAlias = ExecuteMotionPrimitiveSequence_GetResult
        FeedbackMessage: TypeAlias = ExecuteMotionPrimitiveSequence_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
