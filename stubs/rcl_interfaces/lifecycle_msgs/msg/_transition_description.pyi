# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import lifecycle_msgs.msg

class TransitionDescription:
    def __init__(
        self,
        *,
        transition: lifecycle_msgs.msg.Transition = ...,
        start_state: lifecycle_msgs.msg.State = ...,
        goal_state: lifecycle_msgs.msg.State = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def transition(self) -> lifecycle_msgs.msg.Transition: ...
    @transition.setter
    def transition(self, value: lifecycle_msgs.msg.Transition) -> None: ...
    @property
    def start_state(self) -> lifecycle_msgs.msg.State: ...
    @start_state.setter
    def start_state(self, value: lifecycle_msgs.msg.State) -> None: ...
    @property
    def goal_state(self) -> lifecycle_msgs.msg.State: ...
    @goal_state.setter
    def goal_state(self, value: lifecycle_msgs.msg.State) -> None: ...
