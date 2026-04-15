# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class TwistWithCovariance:
    def __init__(
        self,
        *,
        twist: geometry_msgs.msg.Twist = ...,
        covariance: list[float] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def twist(self) -> geometry_msgs.msg.Twist: ...
    @twist.setter
    def twist(self, value: geometry_msgs.msg.Twist) -> None: ...
    @property
    def covariance(self) -> list[float]: ...
    @covariance.setter
    def covariance(self, value: list[float]) -> None: ...
