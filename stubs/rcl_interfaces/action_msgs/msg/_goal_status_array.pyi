# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import action_msgs.msg

class GoalStatusArray:
    def __init__(
        self,
        *,
        status_list: list[action_msgs.msg.GoalStatus] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def status_list(self) -> list[action_msgs.msg.GoalStatus]: ...
    @status_list.setter
    def status_list(self, value: list[action_msgs.msg.GoalStatus]) -> None: ...
