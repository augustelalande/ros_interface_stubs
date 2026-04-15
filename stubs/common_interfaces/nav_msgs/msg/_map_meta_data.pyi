# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg
import geometry_msgs.msg

class MapMetaData:
    def __init__(
        self,
        *,
        map_load_time: builtin_interfaces.msg.Time = ...,
        resolution: float = ...,
        width: int = ...,
        height: int = ...,
        origin: geometry_msgs.msg.Pose = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def map_load_time(self) -> builtin_interfaces.msg.Time: ...
    @map_load_time.setter
    def map_load_time(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def resolution(self) -> float: ...
    @resolution.setter
    def resolution(self, value: float) -> None: ...
    @property
    def width(self) -> int: ...
    @width.setter
    def width(self, value: int) -> None: ...
    @property
    def height(self) -> int: ...
    @height.setter
    def height(self, value: int) -> None: ...
    @property
    def origin(self) -> geometry_msgs.msg.Pose: ...
    @origin.setter
    def origin(self, value: geometry_msgs.msg.Pose) -> None: ...
