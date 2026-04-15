# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

class GetParameterTypes_Request:
    def __init__(self, *, names: list[str] = ..., check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def names(self) -> list[str]: ...
    @names.setter
    def names(self, value: list[str]) -> None: ...

class GetParameterTypes_Response:
    def __init__(self, *, types: list[int] = ..., check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def types(self) -> list[int]: ...
    @types.setter
    def types(self, value: list[int]) -> None: ...

class GetParameterTypes:
    Request: TypeAlias = GetParameterTypes_Request
    Response: TypeAlias = GetParameterTypes_Response
