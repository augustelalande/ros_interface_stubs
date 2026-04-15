# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import diagnostic_msgs.msg

class SelfTest_Request:
    def __init__(self, *, check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class SelfTest_Response:
    def __init__(
        self,
        *,
        id: str = ...,
        passed: bytes = ...,
        status: list[diagnostic_msgs.msg.DiagnosticStatus] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @property
    def passed(self) -> bytes: ...
    @passed.setter
    def passed(self, value: bytes) -> None: ...
    @property
    def status(self) -> list[diagnostic_msgs.msg.DiagnosticStatus]: ...
    @status.setter
    def status(self, value: list[diagnostic_msgs.msg.DiagnosticStatus]) -> None: ...

class SelfTest:
    Request: TypeAlias = SelfTest_Request
    Response: TypeAlias = SelfTest_Response
