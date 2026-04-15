# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class GridCells:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        cell_width: float = ...,
        cell_height: float = ...,
        cells: list[geometry_msgs.msg.Point] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def cell_width(self) -> float: ...
    @cell_width.setter
    def cell_width(self, value: float) -> None: ...
    @property
    def cell_height(self) -> float: ...
    @cell_height.setter
    def cell_height(self, value: float) -> None: ...
    @property
    def cells(self) -> list[geometry_msgs.msg.Point]: ...
    @cells.setter
    def cells(self, value: list[geometry_msgs.msg.Point]) -> None: ...
