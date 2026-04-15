# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class JointState:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        name: list[str] = ...,
        position: list[float] = ...,
        velocity: list[float] = ...,
        effort: list[float] = ...,
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
    def name(self) -> list[str]: ...
    @name.setter
    def name(self, value: list[str]) -> None: ...
    @property
    def position(self) -> list[float]: ...
    @position.setter
    def position(self, value: list[float]) -> None: ...
    @property
    def velocity(self) -> list[float]: ...
    @velocity.setter
    def velocity(self, value: list[float]) -> None: ...
    @property
    def effort(self) -> list[float]: ...
    @effort.setter
    def effort(self, value: list[float]) -> None: ...
