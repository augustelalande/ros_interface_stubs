# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import rcl_interfaces.msg

class SetParameters_Request:
    def __init__(
        self,
        *,
        parameters: list[rcl_interfaces.msg.Parameter] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def parameters(self) -> list[rcl_interfaces.msg.Parameter]: ...
    @parameters.setter
    def parameters(self, value: list[rcl_interfaces.msg.Parameter]) -> None: ...

class SetParameters_Response:
    def __init__(
        self,
        *,
        results: list[rcl_interfaces.msg.SetParametersResult] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def results(self) -> list[rcl_interfaces.msg.SetParametersResult]: ...
    @results.setter
    def results(self, value: list[rcl_interfaces.msg.SetParametersResult]) -> None: ...

class SetParameters:
    Request: TypeAlias = SetParameters_Request
    Response: TypeAlias = SetParameters_Response
