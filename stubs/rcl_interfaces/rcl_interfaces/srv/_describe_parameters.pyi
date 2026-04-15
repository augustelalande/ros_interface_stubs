# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import rcl_interfaces.msg

class DescribeParameters_Request:
    def __init__(
        self,
        *,
        names: list[str] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def names(self) -> list[str]: ...
    @names.setter
    def names(self, value: list[str]) -> None: ...

class DescribeParameters_Response:
    def __init__(
        self,
        *,
        descriptors: list[rcl_interfaces.msg.ParameterDescriptor] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def descriptors(self) -> list[rcl_interfaces.msg.ParameterDescriptor]: ...
    @descriptors.setter
    def descriptors(
        self, value: list[rcl_interfaces.msg.ParameterDescriptor]
    ) -> None: ...

class DescribeParameters:
    Request: TypeAlias = DescribeParameters_Request
    Response: TypeAlias = DescribeParameters_Response
