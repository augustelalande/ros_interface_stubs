# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class Joy:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        axes: list[float] = ...,
        buttons: list[int] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def axes(self) -> list[float]: ...
    @axes.setter
    def axes(self, value: list[float]) -> None: ...
    @property
    def buttons(self) -> list[int]: ...
    @buttons.setter
    def buttons(self, value: list[int]) -> None: ...
