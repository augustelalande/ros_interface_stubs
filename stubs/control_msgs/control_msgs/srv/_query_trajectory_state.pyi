# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import builtin_interfaces.msg

class QueryTrajectoryState_Request:
    def __init__(
        self,
        *,
        time: builtin_interfaces.msg.Time = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def time(self) -> builtin_interfaces.msg.Time: ...
    @time.setter
    def time(self, value: builtin_interfaces.msg.Time) -> None: ...

class QueryTrajectoryState_Response:
    def __init__(
        self,
        *,
        success: bool = ...,
        message: str = ...,
        name: list[str] = ...,
        position: list[float] = ...,
        velocity: list[float] = ...,
        acceleration: list[float] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str) -> None: ...
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
    def acceleration(self) -> list[float]: ...
    @acceleration.setter
    def acceleration(self, value: list[float]) -> None: ...

class QueryTrajectoryState:
    Request: TypeAlias = QueryTrajectoryState_Request
    Response: TypeAlias = QueryTrajectoryState_Response
