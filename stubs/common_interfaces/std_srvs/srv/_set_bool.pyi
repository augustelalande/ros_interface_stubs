# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

class SetBool_Request:
    def __init__(self, *, data: bool = ..., check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def data(self) -> bool: ...
    @data.setter
    def data(self, value: bool) -> None: ...

class SetBool_Response:
    def __init__(
        self, *, success: bool = ..., message: str = ..., check_fields: bool = ...
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str) -> None: ...

class SetBool:
    Request: TypeAlias = SetBool_Request
    Response: TypeAlias = SetBool_Response
