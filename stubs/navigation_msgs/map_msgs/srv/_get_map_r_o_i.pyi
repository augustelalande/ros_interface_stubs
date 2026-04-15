# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import nav_msgs.msg

class GetMapROI_Request:
    def __init__(
        self,
        *,
        x: float = ...,
        y: float = ...,
        l_x: float = ...,
        l_y: float = ...,
        check_fields: bool = ...,
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
    def l_x(self) -> float: ...
    @l_x.setter
    def l_x(self, value: float) -> None: ...
    @property
    def l_y(self) -> float: ...
    @l_y.setter
    def l_y(self, value: float) -> None: ...

class GetMapROI_Response:
    def __init__(
        self,
        *,
        sub_map: nav_msgs.msg.OccupancyGrid = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def sub_map(self) -> nav_msgs.msg.OccupancyGrid: ...
    @sub_map.setter
    def sub_map(self, value: nav_msgs.msg.OccupancyGrid) -> None: ...

class GetMapROI:
    Request: TypeAlias = GetMapROI_Request
    Response: TypeAlias = GetMapROI_Response
