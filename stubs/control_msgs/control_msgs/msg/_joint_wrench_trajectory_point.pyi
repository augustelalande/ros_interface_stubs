# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg
import trajectory_msgs.msg

class JointWrenchTrajectoryPoint:
    def __init__(
        self,
        *,
        point: trajectory_msgs.msg.JointTrajectoryPoint = ...,
        wrench: control_msgs.msg.WrenchFramed = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def point(self) -> trajectory_msgs.msg.JointTrajectoryPoint: ...
    @point.setter
    def point(self, value: trajectory_msgs.msg.JointTrajectoryPoint) -> None: ...
    @property
    def wrench(self) -> control_msgs.msg.WrenchFramed: ...
    @wrench.setter
    def wrench(self, value: control_msgs.msg.WrenchFramed) -> None: ...
