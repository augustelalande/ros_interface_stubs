# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import action_msgs.msg

class CancelGoal_Request:
    def __init__(
        self, *, goal_info: action_msgs.msg.GoalInfo = ..., check_fields: bool = ...
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def goal_info(self) -> action_msgs.msg.GoalInfo: ...
    @goal_info.setter
    def goal_info(self, value: action_msgs.msg.GoalInfo) -> None: ...

class CancelGoal_Response:
    # Constants

    ERROR_NONE: int = 0

    ERROR_REJECTED: int = 1

    ERROR_UNKNOWN_GOAL_ID: int = 2

    ERROR_GOAL_TERMINATED: int = 3

    def __init__(
        self,
        *,
        return_code: int = ...,
        goals_canceling: list[action_msgs.msg.GoalInfo] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def return_code(self) -> int: ...
    @return_code.setter
    def return_code(self, value: int) -> None: ...
    @property
    def goals_canceling(self) -> list[action_msgs.msg.GoalInfo]: ...
    @goals_canceling.setter
    def goals_canceling(self, value: list[action_msgs.msg.GoalInfo]) -> None: ...

class CancelGoal:
    Request: TypeAlias = CancelGoal_Request
    Response: TypeAlias = CancelGoal_Response
