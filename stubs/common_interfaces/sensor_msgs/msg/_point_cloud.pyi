# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg

class PointCloud:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        points: list[geometry_msgs.msg.Point32] = ...,
        channels: list[sensor_msgs.msg.ChannelFloat32] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def points(self) -> list[geometry_msgs.msg.Point32]: ...
    @points.setter
    def points(self, value: list[geometry_msgs.msg.Point32]) -> None: ...
    @property
    def channels(self) -> list[sensor_msgs.msg.ChannelFloat32]: ...
    @channels.setter
    def channels(self, value: list[sensor_msgs.msg.ChannelFloat32]) -> None: ...
