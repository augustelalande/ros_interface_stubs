# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class GripperCommand:
    def __init__(
        self,
        *,
        position: float = ...,
        max_effort: float = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def position(self) -> float: ...
    @position.setter
    def position(self, value: float) -> None: ...
    @property
    def max_effort(self) -> float: ...
    @max_effort.setter
    def max_effort(self, value: float) -> None: ...
