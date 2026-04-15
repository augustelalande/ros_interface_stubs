# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class Pose:
    def __init__(
        self,
        *,
        position: geometry_msgs.msg.Point = ...,
        orientation: geometry_msgs.msg.Quaternion = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def position(self) -> geometry_msgs.msg.Point: ...
    @position.setter
    def position(self, value: geometry_msgs.msg.Point) -> None: ...
    @property
    def orientation(self) -> geometry_msgs.msg.Quaternion: ...
    @orientation.setter
    def orientation(self, value: geometry_msgs.msg.Quaternion) -> None: ...
