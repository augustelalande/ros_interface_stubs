# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import nav_msgs.msg

class GetMap_Request:
    def __init__(
        self,
        *,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class GetMap_Response:
    def __init__(
        self,
        *,
        map: nav_msgs.msg.OccupancyGrid = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def map(self) -> nav_msgs.msg.OccupancyGrid: ...
    @map.setter
    def map(self, value: nav_msgs.msg.OccupancyGrid) -> None: ...

class GetMap:
    Request: TypeAlias = GetMap_Request
    Response: TypeAlias = GetMap_Response
