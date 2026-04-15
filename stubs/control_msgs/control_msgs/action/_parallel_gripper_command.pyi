# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import builtin_interfaces.msg
import sensor_msgs.msg
import unique_identifier_msgs.msg

class ParallelGripperCommand_Goal:
    def __init__(
        self,
        *,
        command: sensor_msgs.msg.JointState = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def command(self) -> sensor_msgs.msg.JointState: ...
    @command.setter
    def command(self, value: sensor_msgs.msg.JointState) -> None: ...

class ParallelGripperCommand_Result:
    def __init__(
        self,
        *,
        state: sensor_msgs.msg.JointState = ...,
        stalled: bool = ...,
        reached_goal: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def state(self) -> sensor_msgs.msg.JointState: ...
    @state.setter
    def state(self, value: sensor_msgs.msg.JointState) -> None: ...
    @property
    def stalled(self) -> bool: ...
    @stalled.setter
    def stalled(self, value: bool) -> None: ...
    @property
    def reached_goal(self) -> bool: ...
    @reached_goal.setter
    def reached_goal(self, value: bool) -> None: ...

class ParallelGripperCommand_Feedback:
    def __init__(
        self,
        *,
        state: sensor_msgs.msg.JointState = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def state(self) -> sensor_msgs.msg.JointState: ...
    @state.setter
    def state(self, value: sensor_msgs.msg.JointState) -> None: ...

class ParallelGripperCommand_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: ParallelGripperCommand_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> ParallelGripperCommand_Goal: ...
    @goal.setter
    def goal(self, value: ParallelGripperCommand_Goal) -> None: ...

class ParallelGripperCommand_SendGoal_Response:
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

class ParallelGripperCommand_SendGoal:
    Request: TypeAlias = ParallelGripperCommand_SendGoal_Request
    Response: TypeAlias = ParallelGripperCommand_SendGoal_Response

class ParallelGripperCommand_GetResult_Request:
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

class ParallelGripperCommand_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: ParallelGripperCommand_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> ParallelGripperCommand_Result: ...
    @result.setter
    def result(self, value: ParallelGripperCommand_Result) -> None: ...

class ParallelGripperCommand_GetResult:
    Request: TypeAlias = ParallelGripperCommand_GetResult_Request
    Response: TypeAlias = ParallelGripperCommand_GetResult_Response

class ParallelGripperCommand_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: ParallelGripperCommand_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> ParallelGripperCommand_Feedback: ...
    @feedback.setter
    def feedback(self, value: ParallelGripperCommand_Feedback) -> None: ...

class ParallelGripperCommand:
    Goal: TypeAlias = ParallelGripperCommand_Goal
    Result: TypeAlias = ParallelGripperCommand_Result
    Feedback: TypeAlias = ParallelGripperCommand_Feedback

    class Impl:
        SendGoalService: TypeAlias = ParallelGripperCommand_SendGoal
        GetResultService: TypeAlias = ParallelGripperCommand_GetResult
        FeedbackMessage: TypeAlias = ParallelGripperCommand_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
