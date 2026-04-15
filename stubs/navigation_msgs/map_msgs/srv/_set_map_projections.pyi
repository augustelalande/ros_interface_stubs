# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import map_msgs.msg

class SetMapProjections_Request:
    def __init__(self) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class SetMapProjections_Response:
    def __init__(
        self,
        *,
        projected_maps_info: list[map_msgs.msg.ProjectedMapInfo] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def projected_maps_info(self) -> list[map_msgs.msg.ProjectedMapInfo]: ...
    @projected_maps_info.setter
    def projected_maps_info(
        self, value: list[map_msgs.msg.ProjectedMapInfo]
    ) -> None: ...

class SetMapProjections:
    Request: TypeAlias = SetMapProjections_Request
    Response: TypeAlias = SetMapProjections_Response
