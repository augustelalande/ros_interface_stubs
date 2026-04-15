# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import std_msgs.msg

class SaveMap_Request:
    def __init__(
        self,
        *,
        filename: std_msgs.msg.String = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def filename(self) -> std_msgs.msg.String: ...
    @filename.setter
    def filename(self, value: std_msgs.msg.String) -> None: ...

class SaveMap_Response:
    def __init__(
        self,
        *,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members

class SaveMap:
    Request: TypeAlias = SaveMap_Request
    Response: TypeAlias = SaveMap_Response
