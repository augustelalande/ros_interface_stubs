# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class InteractiveMarkerFeedback:
    # Constants
    KEEP_ALIVE: int = 0
    POSE_UPDATE: int = 1
    MENU_SELECT: int = 2
    BUTTON_CLICK: int = 3
    MOUSE_DOWN: int = 4
    MOUSE_UP: int = 5

    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        client_id: str = ...,
        marker_name: str = ...,
        control_name: str = ...,
        event_type: int = ...,
        pose: geometry_msgs.msg.Pose = ...,
        menu_entry_id: int = ...,
        mouse_point: geometry_msgs.msg.Point = ...,
        mouse_point_valid: bool = ...,
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
    def client_id(self) -> str: ...
    @client_id.setter
    def client_id(self, value: str) -> None: ...
    @property
    def marker_name(self) -> str: ...
    @marker_name.setter
    def marker_name(self, value: str) -> None: ...
    @property
    def control_name(self) -> str: ...
    @control_name.setter
    def control_name(self, value: str) -> None: ...
    @property
    def event_type(self) -> int: ...
    @event_type.setter
    def event_type(self, value: int) -> None: ...
    @property
    def pose(self) -> geometry_msgs.msg.Pose: ...
    @pose.setter
    def pose(self, value: geometry_msgs.msg.Pose) -> None: ...
    @property
    def menu_entry_id(self) -> int: ...
    @menu_entry_id.setter
    def menu_entry_id(self, value: int) -> None: ...
    @property
    def mouse_point(self) -> geometry_msgs.msg.Point: ...
    @mouse_point.setter
    def mouse_point(self, value: geometry_msgs.msg.Point) -> None: ...
    @property
    def mouse_point_valid(self) -> bool: ...
    @mouse_point_valid.setter
    def mouse_point_valid(self, value: bool) -> None: ...
