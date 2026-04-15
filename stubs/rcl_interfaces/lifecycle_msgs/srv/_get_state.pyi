# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import lifecycle_msgs.msg

class GetState_Request:
    def __init__(self, *, check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class GetState_Response:
    def __init__(
        self, *, current_state: lifecycle_msgs.msg.State = ..., check_fields: bool = ...
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def current_state(self) -> lifecycle_msgs.msg.State: ...
    @current_state.setter
    def current_state(self, value: lifecycle_msgs.msg.State) -> None: ...

class GetState:
    Request: TypeAlias = GetState_Request
    Response: TypeAlias = GetState_Response
