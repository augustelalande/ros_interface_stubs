# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import sensor_msgs.msg

class GetPointMapROI_Request:
    def __init__(
        self,
        *,
        x: float = ...,
        y: float = ...,
        z: float = ...,
        r: float = ...,
        l_x: float = ...,
        l_y: float = ...,
        l_z: float = ...,
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
    def r(self) -> float: ...
    @r.setter
    def r(self, value: float) -> None: ...
    @property
    def l_x(self) -> float: ...
    @l_x.setter
    def l_x(self, value: float) -> None: ...
    @property
    def l_y(self) -> float: ...
    @l_y.setter
    def l_y(self, value: float) -> None: ...
    @property
    def l_z(self) -> float: ...
    @l_z.setter
    def l_z(self, value: float) -> None: ...

class GetPointMapROI_Response:
    def __init__(
        self,
        *,
        sub_map: sensor_msgs.msg.PointCloud2 = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def sub_map(self) -> sensor_msgs.msg.PointCloud2: ...
    @sub_map.setter
    def sub_map(self, value: sensor_msgs.msg.PointCloud2) -> None: ...

class GetPointMapROI:
    Request: TypeAlias = GetPointMapROI_Request
    Response: TypeAlias = GetPointMapROI_Response
