# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class FloatingPointRange:
    def __init__(
        self,
        *,
        from_value: float = ...,
        to_value: float = ...,
        step: float = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def from_value(self) -> float: ...
    @from_value.setter
    def from_value(self, value: float) -> None: ...
    @property
    def to_value(self) -> float: ...
    @to_value.setter
    def to_value(self, value: float) -> None: ...
    @property
    def step(self) -> float: ...
    @step.setter
    def step(self, value: float) -> None: ...
