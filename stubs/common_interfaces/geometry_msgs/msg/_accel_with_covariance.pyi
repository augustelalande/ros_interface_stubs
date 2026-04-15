# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class AccelWithCovariance:
    def __init__(
        self,
        *,
        accel: geometry_msgs.msg.Accel = ...,
        covariance: list[float] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def accel(self) -> geometry_msgs.msg.Accel: ...
    @accel.setter
    def accel(self, value: geometry_msgs.msg.Accel) -> None: ...
    @property
    def covariance(self) -> list[float]: ...
    @covariance.setter
    def covariance(self, value: list[float]) -> None: ...
