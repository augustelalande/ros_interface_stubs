# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg
import visualization_msgs.msg

class InteractiveMarker:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        pose: geometry_msgs.msg.Pose = ...,
        name: str = ...,
        description: str = ...,
        scale: float = ...,
        menu_entries: list[visualization_msgs.msg.MenuEntry] = ...,
        controls: list[visualization_msgs.msg.InteractiveMarkerControl] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def pose(self) -> geometry_msgs.msg.Pose: ...
    @pose.setter
    def pose(self, value: geometry_msgs.msg.Pose) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...
    @property
    def scale(self) -> float: ...
    @scale.setter
    def scale(self, value: float) -> None: ...
    @property
    def menu_entries(self) -> list[visualization_msgs.msg.MenuEntry]: ...
    @menu_entries.setter
    def menu_entries(self, value: list[visualization_msgs.msg.MenuEntry]) -> None: ...
    @property
    def controls(self) -> list[visualization_msgs.msg.InteractiveMarkerControl]: ...
    @controls.setter
    def controls(
        self, value: list[visualization_msgs.msg.InteractiveMarkerControl]
    ) -> None: ...
