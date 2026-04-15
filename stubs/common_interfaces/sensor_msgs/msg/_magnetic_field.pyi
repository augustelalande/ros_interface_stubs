# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class MagneticField:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        magnetic_field: geometry_msgs.msg.Vector3 = ...,
        magnetic_field_covariance: list[float] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def magnetic_field(self) -> geometry_msgs.msg.Vector3: ...
    @magnetic_field.setter
    def magnetic_field(self, value: geometry_msgs.msg.Vector3) -> None: ...
    @property
    def magnetic_field_covariance(self) -> list[float]: ...
    @magnetic_field_covariance.setter
    def magnetic_field_covariance(self, value: list[float]) -> None: ...
