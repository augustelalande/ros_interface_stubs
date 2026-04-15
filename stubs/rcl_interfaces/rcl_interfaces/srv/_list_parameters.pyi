# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import rcl_interfaces.msg

class ListParameters_Request:
    # Constants

    DEPTH_RECURSIVE: int = 0

    def __init__(
        self, *, prefixes: list[str] = ..., depth: int = ..., check_fields: bool = ...
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def prefixes(self) -> list[str]: ...
    @prefixes.setter
    def prefixes(self, value: list[str]) -> None: ...
    @property
    def depth(self) -> int: ...
    @depth.setter
    def depth(self, value: int) -> None: ...

class ListParameters_Response:
    def __init__(
        self,
        *,
        result: rcl_interfaces.msg.ListParametersResult = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def result(self) -> rcl_interfaces.msg.ListParametersResult: ...
    @result.setter
    def result(self, value: rcl_interfaces.msg.ListParametersResult) -> None: ...

class ListParameters:
    Request: TypeAlias = ListParameters_Request
    Response: TypeAlias = ListParameters_Response
