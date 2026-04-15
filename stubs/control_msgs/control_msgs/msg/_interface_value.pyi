# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class InterfaceValue:
    def __init__(
        self,
        *,
        interface_names: list[str] = ...,
        values: list[float] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def interface_names(self) -> list[str]: ...
    @interface_names.setter
    def interface_names(self, value: list[str]) -> None: ...
    @property
    def values(self) -> list[float]: ...
    @values.setter
    def values(self, value: list[float]) -> None: ...
