# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import geometry_msgs.msg
import nav_msgs.msg

class SetMap_Request:
    def __init__(
        self,
        *,
        map: nav_msgs.msg.OccupancyGrid = ...,
        initial_pose: geometry_msgs.msg.PoseWithCovarianceStamped = ...,
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
    def initial_pose(self) -> geometry_msgs.msg.PoseWithCovarianceStamped: ...
    @initial_pose.setter
    def initial_pose(
        self, value: geometry_msgs.msg.PoseWithCovarianceStamped
    ) -> None: ...

class SetMap_Response:
    def __init__(self, *, success: bool = ..., check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class SetMap:
    Request: TypeAlias = SetMap_Request
    Response: TypeAlias = SetMap_Response
