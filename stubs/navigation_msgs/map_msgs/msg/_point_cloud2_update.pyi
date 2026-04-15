# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sensor_msgs.msg
import std_msgs.msg

class PointCloud2Update:
    # Constants
    ADD: int = 0
    DELETE: int = 1

    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        type: int = ...,  # noqa: A002
        points: sensor_msgs.msg.PointCloud2 = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def type(self) -> int: ...
    @type.setter
    def type(self, value: int) -> None: ...
    @property
    def points(self) -> sensor_msgs.msg.PointCloud2: ...
    @points.setter
    def points(self, value: sensor_msgs.msg.PointCloud2) -> None: ...
