# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class Transform:
    def __init__(
        self,
        *,
        translation: geometry_msgs.msg.Vector3 = ...,
        rotation: geometry_msgs.msg.Quaternion = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def translation(self) -> geometry_msgs.msg.Vector3: ...
    @translation.setter
    def translation(self, value: geometry_msgs.msg.Vector3) -> None: ...
    @property
    def rotation(self) -> geometry_msgs.msg.Quaternion: ...
    @rotation.setter
    def rotation(self, value: geometry_msgs.msg.Quaternion) -> None: ...
