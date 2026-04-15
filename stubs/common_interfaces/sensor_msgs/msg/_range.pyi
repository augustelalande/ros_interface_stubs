# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class Range:
    # Constants
    ULTRASOUND: int = 0
    INFRARED: int = 1

    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        radiation_type: int = ...,
        field_of_view: float = ...,
        min_range: float = ...,
        max_range: float = ...,
        range: float = ...,  # noqa: A002
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
    def radiation_type(self) -> int: ...
    @radiation_type.setter
    def radiation_type(self, value: int) -> None: ...
    @property
    def field_of_view(self) -> float: ...
    @field_of_view.setter
    def field_of_view(self, value: float) -> None: ...
    @property
    def min_range(self) -> float: ...
    @min_range.setter
    def min_range(self, value: float) -> None: ...
    @property
    def max_range(self) -> float: ...
    @max_range.setter
    def max_range(self, value: float) -> None: ...
    @property
    def range(self) -> float: ...
    @range.setter
    def range(self, value: float) -> None: ...
    @property
    def variance(self) -> float: ...
    @variance.setter
    def variance(self, value: float) -> None: ...
