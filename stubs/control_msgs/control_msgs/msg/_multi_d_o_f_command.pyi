# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class MultiDOFCommand:
    def __init__(
        self,
        *,
        dof_names: list[str] = ...,
        values: list[float] = ...,
        values_dot: list[float] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def dof_names(self) -> list[str]: ...
    @dof_names.setter
    def dof_names(self, value: list[str]) -> None: ...
    @property
    def values(self) -> list[float]: ...
    @values.setter
    def values(self, value: list[float]) -> None: ...
    @property
    def values_dot(self) -> list[float]: ...
    @values_dot.setter
    def values_dot(self, value: list[float]) -> None: ...
