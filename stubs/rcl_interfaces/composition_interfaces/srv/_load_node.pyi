# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import rcl_interfaces.msg

class LoadNode_Request:
    def __init__(
        self,
        *,
        package_name: str = ...,
        plugin_name: str = ...,
        node_name: str = ...,
        node_namespace: str = ...,
        log_level: int = ...,
        remap_rules: list[str] = ...,
        parameters: list[rcl_interfaces.msg.Parameter] = ...,
        extra_arguments: list[rcl_interfaces.msg.Parameter] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def package_name(self) -> str: ...
    @package_name.setter
    def package_name(self, value: str) -> None: ...
    @property
    def plugin_name(self) -> str: ...
    @plugin_name.setter
    def plugin_name(self, value: str) -> None: ...
    @property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @property
    def log_level(self) -> int: ...
    @log_level.setter
    def log_level(self, value: int) -> None: ...
    @property
    def remap_rules(self) -> list[str]: ...
    @remap_rules.setter
    def remap_rules(self, value: list[str]) -> None: ...
    @property
    def parameters(self) -> list[rcl_interfaces.msg.Parameter]: ...
    @parameters.setter
    def parameters(self, value: list[rcl_interfaces.msg.Parameter]) -> None: ...
    @property
    def extra_arguments(self) -> list[rcl_interfaces.msg.Parameter]: ...
    @extra_arguments.setter
    def extra_arguments(self, value: list[rcl_interfaces.msg.Parameter]) -> None: ...

class LoadNode_Response:
    def __init__(
        self,
        *,
        success: bool = ...,
        error_message: str = ...,
        full_node_name: str = ...,
        unique_id: int = ...,
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
    @property
    def full_node_name(self) -> str: ...
    @full_node_name.setter
    def full_node_name(self, value: str) -> None: ...
    @property
    def unique_id(self) -> int: ...
    @unique_id.setter
    def unique_id(self, value: int) -> None: ...

class LoadNode:
    Request: TypeAlias = LoadNode_Request
    Response: TypeAlias = LoadNode_Response
