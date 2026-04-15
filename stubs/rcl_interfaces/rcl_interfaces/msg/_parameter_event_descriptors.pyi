# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import rcl_interfaces.msg

class ParameterEventDescriptors:
    def __init__(
        self,
        *,
        new_parameters: list[rcl_interfaces.msg.ParameterDescriptor] = ...,
        changed_parameters: list[rcl_interfaces.msg.ParameterDescriptor] = ...,
        deleted_parameters: list[rcl_interfaces.msg.ParameterDescriptor] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def new_parameters(self) -> list[rcl_interfaces.msg.ParameterDescriptor]: ...
    @new_parameters.setter
    def new_parameters(
        self, value: list[rcl_interfaces.msg.ParameterDescriptor]
    ) -> None: ...
    @property
    def changed_parameters(self) -> list[rcl_interfaces.msg.ParameterDescriptor]: ...
    @changed_parameters.setter
    def changed_parameters(
        self, value: list[rcl_interfaces.msg.ParameterDescriptor]
    ) -> None: ...
    @property
    def deleted_parameters(self) -> list[rcl_interfaces.msg.ParameterDescriptor]: ...
    @deleted_parameters.setter
    def deleted_parameters(
        self, value: list[rcl_interfaces.msg.ParameterDescriptor]
    ) -> None: ...
