# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import lifecycle_msgs.msg

class ChangeState_Request:
    def __init__(
        self,
        *,
        transition: lifecycle_msgs.msg.Transition = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def transition(self) -> lifecycle_msgs.msg.Transition: ...
    @transition.setter
    def transition(self, value: lifecycle_msgs.msg.Transition) -> None: ...

class ChangeState_Response:
    def __init__(
        self,
        *,
        success: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class ChangeState:
    Request: TypeAlias = ChangeState_Request
    Response: TypeAlias = ChangeState_Response
