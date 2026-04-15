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

class GripperCommand_Goal:
    def __init__(
        self,
        *,
        command: control_msgs.msg.GripperCommand = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def command(self) -> control_msgs.msg.GripperCommand: ...
    @command.setter
    def command(self, value: control_msgs.msg.GripperCommand) -> None: ...

class GripperCommand_Result:
    def __init__(
        self,
        *,
        position: float = ...,
        effort: float = ...,
        stalled: bool = ...,
        reached_goal: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def position(self) -> float: ...
    @position.setter
    def position(self, value: float) -> None: ...
    @property
    def effort(self) -> float: ...
    @effort.setter
    def effort(self, value: float) -> None: ...
    @property
    def stalled(self) -> bool: ...
    @stalled.setter
    def stalled(self, value: bool) -> None: ...
    @property
    def reached_goal(self) -> bool: ...
    @reached_goal.setter
    def reached_goal(self, value: bool) -> None: ...

class GripperCommand_Feedback:
    def __init__(
        self,
        *,
        position: float = ...,
        effort: float = ...,
        stalled: bool = ...,
        reached_goal: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def position(self) -> float: ...
    @position.setter
    def position(self, value: float) -> None: ...
    @property
    def effort(self) -> float: ...
    @effort.setter
    def effort(self, value: float) -> None: ...
    @property
    def stalled(self) -> bool: ...
    @stalled.setter
    def stalled(self, value: bool) -> None: ...
    @property
    def reached_goal(self) -> bool: ...
    @reached_goal.setter
    def reached_goal(self, value: bool) -> None: ...

class GripperCommand_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: GripperCommand_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> GripperCommand_Goal: ...
    @goal.setter
    def goal(self, value: GripperCommand_Goal) -> None: ...

class GripperCommand_SendGoal_Response:
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

class GripperCommand_SendGoal:
    Request: TypeAlias = GripperCommand_SendGoal_Request
    Response: TypeAlias = GripperCommand_SendGoal_Response

class GripperCommand_GetResult_Request:
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

class GripperCommand_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: GripperCommand_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> GripperCommand_Result: ...
    @result.setter
    def result(self, value: GripperCommand_Result) -> None: ...

class GripperCommand_GetResult:
    Request: TypeAlias = GripperCommand_GetResult_Request
    Response: TypeAlias = GripperCommand_GetResult_Response

class GripperCommand_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: GripperCommand_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> GripperCommand_Feedback: ...
    @feedback.setter
    def feedback(self, value: GripperCommand_Feedback) -> None: ...

class GripperCommand:
    Goal: TypeAlias = GripperCommand_Goal
    Result: TypeAlias = GripperCommand_Result
    Feedback: TypeAlias = GripperCommand_Feedback

    class Impl:
        SendGoalService: TypeAlias = GripperCommand_SendGoal
        GetResultService: TypeAlias = GripperCommand_GetResult
        FeedbackMessage: TypeAlias = GripperCommand_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
