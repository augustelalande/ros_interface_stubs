# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class PoseWithCovariance:
    def __init__(
        self,
        *,
        pose: geometry_msgs.msg.Pose = ...,
        covariance: list[float] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def pose(self) -> geometry_msgs.msg.Pose: ...
    @pose.setter
    def pose(self, value: geometry_msgs.msg.Pose) -> None: ...
    @property
    def covariance(self) -> list[float]: ...
    @covariance.setter
    def covariance(self, value: list[float]) -> None: ...
