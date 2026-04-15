# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import builtin_interfaces.msg
import test_msgs.msg
import unique_identifier_msgs.msg

class NestedMessage_Goal:
    def __init__(
        self,
        *,
        nested_field_no_pkg: test_msgs.msg.Builtins = ...,
        nested_field: test_msgs.msg.BasicTypes = ...,
        nested_different_pkg: builtin_interfaces.msg.Time = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def nested_field_no_pkg(self) -> test_msgs.msg.Builtins: ...
    @nested_field_no_pkg.setter
    def nested_field_no_pkg(self, value: test_msgs.msg.Builtins) -> None: ...
    @property
    def nested_field(self) -> test_msgs.msg.BasicTypes: ...
    @nested_field.setter
    def nested_field(self, value: test_msgs.msg.BasicTypes) -> None: ...
    @property
    def nested_different_pkg(self) -> builtin_interfaces.msg.Time: ...
    @nested_different_pkg.setter
    def nested_different_pkg(self, value: builtin_interfaces.msg.Time) -> None: ...

class NestedMessage_Result:
    def __init__(
        self,
        *,
        nested_field_no_pkg: test_msgs.msg.Builtins = ...,
        nested_field: test_msgs.msg.BasicTypes = ...,
        nested_different_pkg: builtin_interfaces.msg.Time = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def nested_field_no_pkg(self) -> test_msgs.msg.Builtins: ...
    @nested_field_no_pkg.setter
    def nested_field_no_pkg(self, value: test_msgs.msg.Builtins) -> None: ...
    @property
    def nested_field(self) -> test_msgs.msg.BasicTypes: ...
    @nested_field.setter
    def nested_field(self, value: test_msgs.msg.BasicTypes) -> None: ...
    @property
    def nested_different_pkg(self) -> builtin_interfaces.msg.Time: ...
    @nested_different_pkg.setter
    def nested_different_pkg(self, value: builtin_interfaces.msg.Time) -> None: ...

class NestedMessage_Feedback:
    def __init__(
        self,
        *,
        nested_field_no_pkg: test_msgs.msg.Builtins = ...,
        nested_field: test_msgs.msg.BasicTypes = ...,
        nested_different_pkg: builtin_interfaces.msg.Time = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def nested_field_no_pkg(self) -> test_msgs.msg.Builtins: ...
    @nested_field_no_pkg.setter
    def nested_field_no_pkg(self, value: test_msgs.msg.Builtins) -> None: ...
    @property
    def nested_field(self) -> test_msgs.msg.BasicTypes: ...
    @nested_field.setter
    def nested_field(self, value: test_msgs.msg.BasicTypes) -> None: ...
    @property
    def nested_different_pkg(self) -> builtin_interfaces.msg.Time: ...
    @nested_different_pkg.setter
    def nested_different_pkg(self, value: builtin_interfaces.msg.Time) -> None: ...

class NestedMessage_SendGoal_Request:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        goal: NestedMessage_Goal = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def goal(self) -> NestedMessage_Goal: ...
    @goal.setter
    def goal(self, value: NestedMessage_Goal) -> None: ...

class NestedMessage_SendGoal_Response:
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

class NestedMessage_SendGoal:
    Request: TypeAlias = NestedMessage_SendGoal_Request
    Response: TypeAlias = NestedMessage_SendGoal_Response

class NestedMessage_GetResult_Request:
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

class NestedMessage_GetResult_Response:
    def __init__(
        self,
        *,
        status: int = ...,
        result: NestedMessage_Result = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def result(self) -> NestedMessage_Result: ...
    @result.setter
    def result(self, value: NestedMessage_Result) -> None: ...

class NestedMessage_GetResult:
    Request: TypeAlias = NestedMessage_GetResult_Request
    Response: TypeAlias = NestedMessage_GetResult_Response

class NestedMessage_FeedbackMessage:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        feedback: NestedMessage_Feedback = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def feedback(self) -> NestedMessage_Feedback: ...
    @feedback.setter
    def feedback(self, value: NestedMessage_Feedback) -> None: ...

class NestedMessage:
    Goal: TypeAlias = NestedMessage_Goal
    Result: TypeAlias = NestedMessage_Result
    Feedback: TypeAlias = NestedMessage_Feedback

    class Impl:
        SendGoalService: TypeAlias = NestedMessage_SendGoal
        GetResultService: TypeAlias = NestedMessage_GetResult
        FeedbackMessage: TypeAlias = NestedMessage_FeedbackMessage

        from action_msgs.msg._goal_status_array import (
            GoalStatusArray as GoalStatusMessage,
        )
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
