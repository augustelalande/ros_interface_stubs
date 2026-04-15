# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class Time:
    def __init__(
        self,
        *,
        sec: int = ...,
        nanosec: int = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def sec(self) -> int: ...
    @sec.setter
    def sec(self, value: int) -> None: ...
    @property
    def nanosec(self) -> int: ...
    @nanosec.setter
    def nanosec(self, value: int) -> None: ...
