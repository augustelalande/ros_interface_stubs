# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import visualization_msgs.msg

class GetInteractiveMarkers_Request:
    def __init__(
        self,
        *,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class GetInteractiveMarkers_Response:
    def __init__(
        self,
        *,
        sequence_number: int = ...,
        markers: list[visualization_msgs.msg.InteractiveMarker] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def sequence_number(self) -> int: ...
    @sequence_number.setter
    def sequence_number(self, value: int) -> None: ...
    @property
    def markers(self) -> list[visualization_msgs.msg.InteractiveMarker]: ...
    @markers.setter
    def markers(
        self, value: list[visualization_msgs.msg.InteractiveMarker]
    ) -> None: ...

class GetInteractiveMarkers:
    Request: TypeAlias = GetInteractiveMarkers_Request
    Response: TypeAlias = GetInteractiveMarkers_Response
