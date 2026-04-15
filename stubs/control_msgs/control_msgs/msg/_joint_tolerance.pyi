# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class JointTolerance:
    def __init__(
        self,
        *,
        name: str = ...,
        position: float = ...,
        velocity: float = ...,
        acceleration: float = ...,
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
    def position(self) -> float: ...
    @position.setter
    def position(self, value: float) -> None: ...
    @property
    def velocity(self) -> float: ...
    @velocity.setter
    def velocity(self, value: float) -> None: ...
    @property
    def acceleration(self) -> float: ...
    @acceleration.setter
    def acceleration(self, value: float) -> None: ...
