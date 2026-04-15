# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import type_description_interfaces.msg

class TypeDescription:
    def __init__(
        self,
        *,
        type_description: type_description_interfaces.msg.IndividualTypeDescription = ...,
        referenced_type_descriptions: list[
            type_description_interfaces.msg.IndividualTypeDescription
        ] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def type_description(
        self,
    ) -> type_description_interfaces.msg.IndividualTypeDescription: ...
    @type_description.setter
    def type_description(
        self, value: type_description_interfaces.msg.IndividualTypeDescription
    ) -> None: ...
    @property
    def referenced_type_descriptions(
        self,
    ) -> list[type_description_interfaces.msg.IndividualTypeDescription]: ...
    @referenced_type_descriptions.setter
    def referenced_type_descriptions(
        self, value: list[type_description_interfaces.msg.IndividualTypeDescription]
    ) -> None: ...
