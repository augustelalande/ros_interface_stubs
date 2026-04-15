# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import type_description_interfaces.msg

class Field:
    def __init__(
        self,
        *,
        name: str = ...,
        type: type_description_interfaces.msg.FieldType = ...,  # noqa: A002
        default_value: str = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def type(self) -> type_description_interfaces.msg.FieldType: ...
    @type.setter
    def type(self, value: type_description_interfaces.msg.FieldType) -> None: ...
    @property
    def default_value(self) -> str: ...
    @default_value.setter
    def default_value(self, value: str) -> None: ...
