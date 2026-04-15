# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import type_description_interfaces.msg

class IndividualTypeDescription:
    def __init__(
        self,
        *,
        type_name: str = ...,
        fields: list[type_description_interfaces.msg.Field] = ...,
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
    def fields(self) -> list[type_description_interfaces.msg.Field]: ...
    @fields.setter
    def fields(self, value: list[type_description_interfaces.msg.Field]) -> None: ...
