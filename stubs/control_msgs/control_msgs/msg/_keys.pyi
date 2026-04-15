# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class Keys:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        keys: list[str] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def keys(self) -> list[str]: ...
    @keys.setter
    def keys(self, value: list[str]) -> None: ...
