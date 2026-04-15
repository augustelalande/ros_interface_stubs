# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import rcl_interfaces.msg

class Parameter:
    def __init__(
        self,
        *,
        name: str = ...,
        value: rcl_interfaces.msg.ParameterValue = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def value(self) -> rcl_interfaces.msg.ParameterValue: ...
    @value.setter
    def value(self, value: rcl_interfaces.msg.ParameterValue) -> None: ...
