# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import nav_msgs.msg
import std_msgs.msg

class Trajectory:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        points: list[nav_msgs.msg.TrajectoryPoint] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def points(self) -> list[nav_msgs.msg.TrajectoryPoint]: ...
    @points.setter
    def points(self, value: list[nav_msgs.msg.TrajectoryPoint]) -> None: ...
