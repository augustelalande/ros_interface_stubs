# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg
import rcl_interfaces.msg

class ParameterEvent:
    def __init__(
        self,
        *,
        stamp: builtin_interfaces.msg.Time = ...,
        node: str = ...,
        new_parameters: list[rcl_interfaces.msg.Parameter] = ...,
        changed_parameters: list[rcl_interfaces.msg.Parameter] = ...,
        deleted_parameters: list[rcl_interfaces.msg.Parameter] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def stamp(self) -> builtin_interfaces.msg.Time: ...
    @stamp.setter
    def stamp(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def node(self) -> str: ...
    @node.setter
    def node(self, value: str) -> None: ...
    @property
    def new_parameters(self) -> list[rcl_interfaces.msg.Parameter]: ...
    @new_parameters.setter
    def new_parameters(self, value: list[rcl_interfaces.msg.Parameter]) -> None: ...
    @property
    def changed_parameters(self) -> list[rcl_interfaces.msg.Parameter]: ...
    @changed_parameters.setter
    def changed_parameters(self, value: list[rcl_interfaces.msg.Parameter]) -> None: ...
    @property
    def deleted_parameters(self) -> list[rcl_interfaces.msg.Parameter]: ...
    @deleted_parameters.setter
    def deleted_parameters(self, value: list[rcl_interfaces.msg.Parameter]) -> None: ...
