# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

class AddDiagnostics_Request:
    def __init__(
        self, *, load_namespace: str = ..., check_fields: bool = ...
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def load_namespace(self) -> str: ...
    @load_namespace.setter
    def load_namespace(self, value: str) -> None: ...

class AddDiagnostics_Response:
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

class AddDiagnostics:
    Request: TypeAlias = AddDiagnostics_Request
    Response: TypeAlias = AddDiagnostics_Response
