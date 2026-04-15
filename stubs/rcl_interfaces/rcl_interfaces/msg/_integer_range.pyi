# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class IntegerRange:
    def __init__(
        self,
        *,
        from_value: int = ...,
        to_value: int = ...,
        step: int = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def from_value(self) -> int: ...
    @from_value.setter
    def from_value(self, value: int) -> None: ...
    @property
    def to_value(self) -> int: ...
    @to_value.setter
    def to_value(self, value: int) -> None: ...
    @property
    def step(self) -> int: ...
    @step.setter
    def step(self, value: int) -> None: ...
