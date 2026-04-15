# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg
import unique_identifier_msgs.msg

class GoalInfo:
    def __init__(
        self,
        *,
        goal_id: unique_identifier_msgs.msg.UUID = ...,
        stamp: builtin_interfaces.msg.Time = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID: ...
    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None: ...
    @property
    def stamp(self) -> builtin_interfaces.msg.Time: ...
    @stamp.setter
    def stamp(self, value: builtin_interfaces.msg.Time) -> None: ...
