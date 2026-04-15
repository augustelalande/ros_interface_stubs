# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import type_description_interfaces.msg

class GetTypeDescription_Request:
    def __init__(
        self,
        *,
        type_name: str = ...,
        type_hash: str = ...,
        include_type_sources: bool = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def type_name(self) -> str: ...
    @type_name.setter
    def type_name(self, value: str) -> None: ...
    @property
    def type_hash(self) -> str: ...
    @type_hash.setter
    def type_hash(self, value: str) -> None: ...
    @property
    def include_type_sources(self) -> bool: ...
    @include_type_sources.setter
    def include_type_sources(self, value: bool) -> None: ...

class GetTypeDescription_Response:
    def __init__(
        self,
        *,
        successful: bool = ...,
        failure_reason: str = ...,
        type_description: type_description_interfaces.msg.TypeDescription = ...,
        type_sources: list[type_description_interfaces.msg.TypeSource] = ...,
        extra_information: list[type_description_interfaces.msg.KeyValue] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def successful(self) -> bool: ...
    @successful.setter
    def successful(self, value: bool) -> None: ...
    @property
    def failure_reason(self) -> str: ...
    @failure_reason.setter
    def failure_reason(self, value: str) -> None: ...
    @property
    def type_description(self) -> type_description_interfaces.msg.TypeDescription: ...
    @type_description.setter
    def type_description(
        self, value: type_description_interfaces.msg.TypeDescription
    ) -> None: ...
    @property
    def type_sources(self) -> list[type_description_interfaces.msg.TypeSource]: ...
    @type_sources.setter
    def type_sources(
        self, value: list[type_description_interfaces.msg.TypeSource]
    ) -> None: ...
    @property
    def extra_information(self) -> list[type_description_interfaces.msg.KeyValue]: ...
    @extra_information.setter
    def extra_information(
        self, value: list[type_description_interfaces.msg.KeyValue]
    ) -> None: ...

class GetTypeDescription:
    Request: TypeAlias = GetTypeDescription_Request
    Response: TypeAlias = GetTypeDescription_Response
