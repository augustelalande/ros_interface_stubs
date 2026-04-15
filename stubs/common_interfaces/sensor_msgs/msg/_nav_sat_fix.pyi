# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sensor_msgs.msg
import std_msgs.msg

class NavSatFix:
    # Constants
    COVARIANCE_TYPE_UNKNOWN: int = 0
    COVARIANCE_TYPE_APPROXIMATED: int = 1
    COVARIANCE_TYPE_DIAGONAL_KNOWN: int = 2
    COVARIANCE_TYPE_KNOWN: int = 3

    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        status: sensor_msgs.msg.NavSatStatus = ...,
        latitude: float = ...,
        longitude: float = ...,
        altitude: float = ...,
        position_covariance: list[float] = ...,
        position_covariance_type: int = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def status(self) -> sensor_msgs.msg.NavSatStatus: ...
    @status.setter
    def status(self, value: sensor_msgs.msg.NavSatStatus) -> None: ...
    @property
    def latitude(self) -> float: ...
    @latitude.setter
    def latitude(self, value: float) -> None: ...
    @property
    def longitude(self) -> float: ...
    @longitude.setter
    def longitude(self, value: float) -> None: ...
    @property
    def altitude(self) -> float: ...
    @altitude.setter
    def altitude(self, value: float) -> None: ...
    @property
    def position_covariance(self) -> list[float]: ...
    @position_covariance.setter
    def position_covariance(self, value: list[float]) -> None: ...
    @property
    def position_covariance_type(self) -> int: ...
    @position_covariance_type.setter
    def position_covariance_type(self, value: int) -> None: ...
