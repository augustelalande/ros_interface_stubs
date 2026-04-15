# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class Temperature:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        temperature: float = ...,
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
    def temperature(self) -> float: ...
    @temperature.setter
    def temperature(self, value: float) -> None: ...
    @property
    def variance(self) -> float: ...
    @variance.setter
    def variance(self, value: float) -> None: ...
