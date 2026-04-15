# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import nav_msgs.msg
import std_msgs.msg

class OccupancyGrid:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        info: nav_msgs.msg.MapMetaData = ...,
        data: list[int] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def info(self) -> nav_msgs.msg.MapMetaData: ...
    @info.setter
    def info(self, value: nav_msgs.msg.MapMetaData) -> None: ...
    @property
    def data(self) -> list[int]: ...
    @data.setter
    def data(self, value: list[int]) -> None: ...
