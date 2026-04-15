# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class LaserEcho:
    def __init__(
        self,
        *,
        echoes: list[float] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def echoes(self) -> list[float]: ...
    @echoes.setter
    def echoes(self, value: list[float]) -> None: ...
