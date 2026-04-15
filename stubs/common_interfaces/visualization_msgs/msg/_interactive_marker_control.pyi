# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import visualization_msgs.msg

class InteractiveMarkerControl:
    # Constants
    INHERIT: int = 0
    FIXED: int = 1
    VIEW_FACING: int = 2
    NONE: int = 0
    MENU: int = 1
    BUTTON: int = 2
    MOVE_AXIS: int = 3
    MOVE_PLANE: int = 4
    ROTATE_AXIS: int = 5
    MOVE_ROTATE: int = 6
    MOVE_3D: int = 7
    ROTATE_3D: int = 8
    MOVE_ROTATE_3D: int = 9

    def __init__(
        self,
        *,
        name: str = ...,
        orientation: geometry_msgs.msg.Quaternion = ...,
        orientation_mode: int = ...,
        interaction_mode: int = ...,
        always_visible: bool = ...,
        markers: list[visualization_msgs.msg.Marker] = ...,
        independent_marker_orientation: bool = ...,
        description: str = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def orientation(self) -> geometry_msgs.msg.Quaternion: ...
    @orientation.setter
    def orientation(self, value: geometry_msgs.msg.Quaternion) -> None: ...
    @property
    def orientation_mode(self) -> int: ...
    @orientation_mode.setter
    def orientation_mode(self, value: int) -> None: ...
    @property
    def interaction_mode(self) -> int: ...
    @interaction_mode.setter
    def interaction_mode(self, value: int) -> None: ...
    @property
    def always_visible(self) -> bool: ...
    @always_visible.setter
    def always_visible(self, value: bool) -> None: ...
    @property
    def markers(self) -> list[visualization_msgs.msg.Marker]: ...
    @markers.setter
    def markers(self, value: list[visualization_msgs.msg.Marker]) -> None: ...
    @property
    def independent_marker_orientation(self) -> bool: ...
    @independent_marker_orientation.setter
    def independent_marker_orientation(self, value: bool) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...
