# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class Plane:
    def __init__(
        self,
        *,
        coef: list[float] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def coef(self) -> list[float]: ...
    @coef.setter
    def coef(self, value: list[float]) -> None: ...
