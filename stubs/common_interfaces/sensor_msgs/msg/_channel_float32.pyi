# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class ChannelFloat32:
    def __init__(
        self,
        *,
        name: str = ...,
        values: list[float] = ...,
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
    def values(self) -> list[float]: ...
    @values.setter
    def values(self, value: list[float]) -> None: ...
