# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import shape_msgs.msg

class Mesh:
    def __init__(
        self,
        *,
        triangles: list[shape_msgs.msg.MeshTriangle] = ...,
        vertices: list[geometry_msgs.msg.Point] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def triangles(self) -> list[shape_msgs.msg.MeshTriangle]: ...
    @triangles.setter
    def triangles(self, value: list[shape_msgs.msg.MeshTriangle]) -> None: ...
    @property
    def vertices(self) -> list[geometry_msgs.msg.Point]: ...
    @vertices.setter
    def vertices(self, value: list[geometry_msgs.msg.Point]) -> None: ...
