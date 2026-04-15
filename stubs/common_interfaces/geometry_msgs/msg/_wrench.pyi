# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class Wrench:
    def __init__(
        self,
        *,
        force: geometry_msgs.msg.Vector3 = ...,
        torque: geometry_msgs.msg.Vector3 = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def force(self) -> geometry_msgs.msg.Vector3: ...
    @force.setter
    def force(self, value: geometry_msgs.msg.Vector3) -> None: ...
    @property
    def torque(self) -> geometry_msgs.msg.Vector3: ...
    @torque.setter
    def torque(self, value: geometry_msgs.msg.Vector3) -> None: ...
