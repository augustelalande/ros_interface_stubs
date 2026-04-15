# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class FluidPressure:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        fluid_pressure: float = ...,
        variance: float = ...,
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
    def fluid_pressure(self) -> float: ...
    @fluid_pressure.setter
    def fluid_pressure(self, value: float) -> None: ...
    @property
    def variance(self) -> float: ...
    @variance.setter
    def variance(self, value: float) -> None: ...
