# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class Twist:
    def __init__(
        self,
        *,
        linear: geometry_msgs.msg.Vector3 = ...,
        angular: geometry_msgs.msg.Vector3 = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def linear(self) -> geometry_msgs.msg.Vector3: ...
    @linear.setter
    def linear(self, value: geometry_msgs.msg.Vector3) -> None: ...
    @property
    def angular(self) -> geometry_msgs.msg.Vector3: ...
    @angular.setter
    def angular(self, value: geometry_msgs.msg.Vector3) -> None: ...
