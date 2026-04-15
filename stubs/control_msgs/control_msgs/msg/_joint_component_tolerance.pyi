# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class JointComponentTolerance:
    # Constants
    X_AXIS: int = 1
    Y_AXIS: int = 2
    Z_AXIS: int = 3
    TRANSLATION: int = 4
    ROTATION: int = 5

    def __init__(
        self,
        *,
        joint_name: str = ...,
        component: int = ...,
        position: float = ...,
        velocity: float = ...,
        acceleration: float = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def joint_name(self) -> str: ...
    @joint_name.setter
    def joint_name(self, value: str) -> None: ...
    @property
    def component(self) -> int: ...
    @component.setter
    def component(self, value: int) -> None: ...
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
