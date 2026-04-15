# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import rcl_interfaces.msg

class SetLoggerLevels_Request:
    def __init__(
        self,
        *,
        levels: list[rcl_interfaces.msg.LoggerLevel] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def levels(self) -> list[rcl_interfaces.msg.LoggerLevel]: ...
    @levels.setter
    def levels(self, value: list[rcl_interfaces.msg.LoggerLevel]) -> None: ...

class SetLoggerLevels_Response:
    def __init__(
        self,
        *,
        results: list[rcl_interfaces.msg.SetLoggerLevelsResult] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def results(self) -> list[rcl_interfaces.msg.SetLoggerLevelsResult]: ...
    @results.setter
    def results(
        self, value: list[rcl_interfaces.msg.SetLoggerLevelsResult]
    ) -> None: ...

class SetLoggerLevels:
    Request: TypeAlias = SetLoggerLevels_Request
    Response: TypeAlias = SetLoggerLevels_Response
