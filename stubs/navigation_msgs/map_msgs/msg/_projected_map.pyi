# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import nav_msgs.msg

class ProjectedMap:
    def __init__(
        self,
        *,
        map: nav_msgs.msg.OccupancyGrid = ...,  # noqa: A002
        min_z: float = ...,
        max_z: float = ...,
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
    def min_z(self) -> float: ...
    @min_z.setter
    def min_z(self, value: float) -> None: ...
    @property
    def max_z(self) -> float: ...
    @max_z.setter
    def max_z(self, value: float) -> None: ...
