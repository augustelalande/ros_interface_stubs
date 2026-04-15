# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class CompressedImage:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        format: str = ...,  # noqa: A002
        data: list[int] = ...,
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
    def format(self) -> str: ...
    @format.setter
    def format(self, value: str) -> None: ...
    @property
    def data(self) -> list[int]: ...
    @data.setter
    def data(self, value: list[int]) -> None: ...
