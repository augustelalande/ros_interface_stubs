# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class JointJog:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        joint_names: list[str] = ...,
        displacements: list[float] = ...,
        velocities: list[float] = ...,
        duration: float = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def joint_names(self) -> list[str]: ...
    @joint_names.setter
    def joint_names(self, value: list[str]) -> None: ...
    @property
    def displacements(self) -> list[float]: ...
    @displacements.setter
    def displacements(self, value: list[float]) -> None: ...
    @property
    def velocities(self) -> list[float]: ...
    @velocities.setter
    def velocities(self, value: list[float]) -> None: ...
    @property
    def duration(self) -> float: ...
    @duration.setter
    def duration(self, value: float) -> None: ...
