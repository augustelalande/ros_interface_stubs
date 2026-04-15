# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import nav_msgs.msg

class LoadMap_Request:
    def __init__(self, *, map_url: str = ..., check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def map_url(self) -> str: ...
    @map_url.setter
    def map_url(self, value: str) -> None: ...

class LoadMap_Response:
    # Constants

    RESULT_SUCCESS: int = 0

    RESULT_MAP_DOES_NOT_EXIST: int = 1

    RESULT_INVALID_MAP_DATA: int = 2

    RESULT_INVALID_MAP_METADATA: int = 3

    RESULT_UNDEFINED_FAILURE: int = 255

    def __init__(
        self,
        *,
        map: nav_msgs.msg.OccupancyGrid = ...,
        result: int = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def map(self) -> nav_msgs.msg.OccupancyGrid: ...
    @map.setter
    def map(self, value: nav_msgs.msg.OccupancyGrid) -> None: ...
    @property
    def result(self) -> int: ...
    @result.setter
    def result(self, value: int) -> None: ...

class LoadMap:
    Request: TypeAlias = LoadMap_Request
    Response: TypeAlias = LoadMap_Response
