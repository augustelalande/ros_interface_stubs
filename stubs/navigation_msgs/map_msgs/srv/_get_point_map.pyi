# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import sensor_msgs.msg

class GetPointMap_Request:
    def __init__(self) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class GetPointMap_Response:
    def __init__(
        self,
        *,
        map: sensor_msgs.msg.PointCloud2 = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def map(self) -> sensor_msgs.msg.PointCloud2: ...
    @map.setter
    def map(self, value: sensor_msgs.msg.PointCloud2) -> None: ...

class GetPointMap:
    Request: TypeAlias = GetPointMap_Request
    Response: TypeAlias = GetPointMap_Response
