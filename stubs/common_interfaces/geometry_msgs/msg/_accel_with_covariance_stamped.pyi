# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class AccelWithCovarianceStamped:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        accel: geometry_msgs.msg.AccelWithCovariance = ...,
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
    def accel(self) -> geometry_msgs.msg.AccelWithCovariance: ...
    @accel.setter
    def accel(self, value: geometry_msgs.msg.AccelWithCovariance) -> None: ...
