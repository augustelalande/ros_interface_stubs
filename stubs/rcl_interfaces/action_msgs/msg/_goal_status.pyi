# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import action_msgs.msg

class GoalStatus:
    # Constants
    STATUS_UNKNOWN: int = 0
    STATUS_ACCEPTED: int = 1
    STATUS_EXECUTING: int = 2
    STATUS_CANCELING: int = 3
    STATUS_SUCCEEDED: int = 4
    STATUS_CANCELED: int = 5
    STATUS_ABORTED: int = 6

    def __init__(
        self,
        *,
        goal_info: action_msgs.msg.GoalInfo = ...,
        status: int = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def goal_info(self) -> action_msgs.msg.GoalInfo: ...
    @goal_info.setter
    def goal_info(self, value: action_msgs.msg.GoalInfo) -> None: ...
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
