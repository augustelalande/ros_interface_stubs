# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import lifecycle_msgs.msg

class GetAvailableStates_Request:
    def __init__(self) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class GetAvailableStates_Response:
    def __init__(
        self,
        *,
        available_states: list[lifecycle_msgs.msg.State] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def available_states(self) -> list[lifecycle_msgs.msg.State]: ...
    @available_states.setter
    def available_states(self, value: list[lifecycle_msgs.msg.State]) -> None: ...

class GetAvailableStates:
    Request: TypeAlias = GetAvailableStates_Request
    Response: TypeAlias = GetAvailableStates_Response
