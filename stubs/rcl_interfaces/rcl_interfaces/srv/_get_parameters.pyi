# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import rcl_interfaces.msg

class GetParameters_Request:
    def __init__(self, *, names: list[str] = ..., check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def names(self) -> list[str]: ...
    @names.setter
    def names(self, value: list[str]) -> None: ...

class GetParameters_Response:
    def __init__(
        self,
        *,
        values: list[rcl_interfaces.msg.ParameterValue] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def values(self) -> list[rcl_interfaces.msg.ParameterValue]: ...
    @values.setter
    def values(self, value: list[rcl_interfaces.msg.ParameterValue]) -> None: ...

class GetParameters:
    Request: TypeAlias = GetParameters_Request
    Response: TypeAlias = GetParameters_Response
