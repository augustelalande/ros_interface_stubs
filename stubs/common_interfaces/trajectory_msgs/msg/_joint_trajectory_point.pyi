# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg

class JointTrajectoryPoint:
    def __init__(
        self,
        *,
        positions: list[float] = ...,
        velocities: list[float] = ...,
        accelerations: list[float] = ...,
        effort: list[float] = ...,
        time_from_start: builtin_interfaces.msg.Duration = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def positions(self) -> list[float]: ...
    @positions.setter
    def positions(self, value: list[float]) -> None: ...
    @property
    def velocities(self) -> list[float]: ...
    @velocities.setter
    def velocities(self, value: list[float]) -> None: ...
    @property
    def accelerations(self) -> list[float]: ...
    @accelerations.setter
    def accelerations(self, value: list[float]) -> None: ...
    @property
    def effort(self) -> list[float]: ...
    @effort.setter
    def effort(self, value: list[float]) -> None: ...
    @property
    def time_from_start(self) -> builtin_interfaces.msg.Duration: ...
    @time_from_start.setter
    def time_from_start(self, value: builtin_interfaces.msg.Duration) -> None: ...
