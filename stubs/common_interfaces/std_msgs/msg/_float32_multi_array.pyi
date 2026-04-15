# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class Float32MultiArray:
    def __init__(
        self,
        *,
        layout: std_msgs.msg.MultiArrayLayout = ...,
        data: list[float] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def layout(self) -> std_msgs.msg.MultiArrayLayout: ...
    @layout.setter
    def layout(self, value: std_msgs.msg.MultiArrayLayout) -> None: ...
    @property
    def data(self) -> list[float]: ...
    @data.setter
    def data(self, value: list[float]) -> None: ...
