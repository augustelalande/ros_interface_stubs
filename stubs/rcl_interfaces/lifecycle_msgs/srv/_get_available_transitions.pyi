# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import lifecycle_msgs.msg

class GetAvailableTransitions_Request:
    def __init__(self, *, check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class GetAvailableTransitions_Response:
    def __init__(
        self,
        *,
        available_transitions: list[lifecycle_msgs.msg.TransitionDescription] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def available_transitions(
        self,
    ) -> list[lifecycle_msgs.msg.TransitionDescription]: ...
    @available_transitions.setter
    def available_transitions(
        self, value: list[lifecycle_msgs.msg.TransitionDescription]
    ) -> None: ...

class GetAvailableTransitions:
    Request: TypeAlias = GetAvailableTransitions_Request
    Response: TypeAlias = GetAvailableTransitions_Response
