# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

class SetOdometry_Request:
    def __init__(
        self,
        *,
        x: float = ...,
        y: float = ...,
        z: float = ...,
        roll: float = ...,
        pitch: float = ...,
        yaw: float = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, value: float) -> None: ...
    @property
    def roll(self) -> float: ...
    @roll.setter
    def roll(self, value: float) -> None: ...
    @property
    def pitch(self) -> float: ...
    @pitch.setter
    def pitch(self, value: float) -> None: ...
    @property
    def yaw(self) -> float: ...
    @yaw.setter
    def yaw(self, value: float) -> None: ...

class SetOdometry_Response:
    def __init__(
        self,
        *,
        success: bool = ...,
        message: str = ...,
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

class SetOdometry:
    Request: TypeAlias = SetOdometry_Request
    Response: TypeAlias = SetOdometry_Response
