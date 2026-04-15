# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class PolygonInstance:
    def __init__(
        self,
        *,
        polygon: geometry_msgs.msg.Polygon = ...,
        id: int = ...,  # noqa: A002
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def polygon(self) -> geometry_msgs.msg.Polygon: ...
    @polygon.setter
    def polygon(self, value: geometry_msgs.msg.Polygon) -> None: ...
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, value: int) -> None: ...
