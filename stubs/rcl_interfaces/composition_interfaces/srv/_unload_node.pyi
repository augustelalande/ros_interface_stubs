# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

class UnloadNode_Request:
    def __init__(
        self,
        *,
        unique_id: int = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def unique_id(self) -> int: ...
    @unique_id.setter
    def unique_id(self, value: int) -> None: ...

class UnloadNode_Response:
    def __init__(
        self,
        *,
        success: bool = ...,
        error_message: str = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...
    @property
    def error_message(self) -> str: ...
    @error_message.setter
    def error_message(self, value: str) -> None: ...

class UnloadNode:
    Request: TypeAlias = UnloadNode_Request
    Response: TypeAlias = UnloadNode_Response
