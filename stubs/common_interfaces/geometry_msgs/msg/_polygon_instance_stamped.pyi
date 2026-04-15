# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class PolygonInstanceStamped:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        polygon: geometry_msgs.msg.PolygonInstance = ...,
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
    def polygon(self) -> geometry_msgs.msg.PolygonInstance: ...
    @polygon.setter
    def polygon(self, value: geometry_msgs.msg.PolygonInstance) -> None: ...
