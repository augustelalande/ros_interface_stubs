# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg
import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg
import visualization_msgs.msg

class Marker:
    # Constants
    ARROW: int = 0
    CUBE: int = 1
    SPHERE: int = 2
    CYLINDER: int = 3
    LINE_STRIP: int = 4
    LINE_LIST: int = 5
    CUBE_LIST: int = 6
    SPHERE_LIST: int = 7
    POINTS: int = 8
    TEXT_VIEW_FACING: int = 9
    MESH_RESOURCE: int = 10
    TRIANGLE_LIST: int = 11
    ARROW_STRIP: int = 12
    ADD: int = 0
    MODIFY: int = 0
    DELETE: int = 2
    DELETEALL: int = 3

    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        ns: str = ...,
        id: int = ...,  # noqa: A002
        type: int = ...,  # noqa: A002
        action: int = ...,
        pose: geometry_msgs.msg.Pose = ...,
        scale: geometry_msgs.msg.Vector3 = ...,
        color: std_msgs.msg.ColorRGBA = ...,
        lifetime: builtin_interfaces.msg.Duration = ...,
        frame_locked: bool = ...,
        points: list[geometry_msgs.msg.Point] = ...,
        colors: list[std_msgs.msg.ColorRGBA] = ...,
        texture_resource: str = ...,
        texture: sensor_msgs.msg.CompressedImage = ...,
        uv_coordinates: list[visualization_msgs.msg.UVCoordinate] = ...,
        text: str = ...,
        mesh_resource: str = ...,
        mesh_file: visualization_msgs.msg.MeshFile = ...,
        mesh_use_embedded_materials: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def ns(self) -> str: ...
    @ns.setter
    def ns(self, value: str) -> None: ...
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, value: int) -> None: ...
    @property
    def type(self) -> int: ...
    @type.setter
    def type(self, value: int) -> None: ...
    @property
    def action(self) -> int: ...
    @action.setter
    def action(self, value: int) -> None: ...
    @property
    def pose(self) -> geometry_msgs.msg.Pose: ...
    @pose.setter
    def pose(self, value: geometry_msgs.msg.Pose) -> None: ...
    @property
    def scale(self) -> geometry_msgs.msg.Vector3: ...
    @scale.setter
    def scale(self, value: geometry_msgs.msg.Vector3) -> None: ...
    @property
    def color(self) -> std_msgs.msg.ColorRGBA: ...
    @color.setter
    def color(self, value: std_msgs.msg.ColorRGBA) -> None: ...
    @property
    def lifetime(self) -> builtin_interfaces.msg.Duration: ...
    @lifetime.setter
    def lifetime(self, value: builtin_interfaces.msg.Duration) -> None: ...
    @property
    def frame_locked(self) -> bool: ...
    @frame_locked.setter
    def frame_locked(self, value: bool) -> None: ...
    @property
    def points(self) -> list[geometry_msgs.msg.Point]: ...
    @points.setter
    def points(self, value: list[geometry_msgs.msg.Point]) -> None: ...
    @property
    def colors(self) -> list[std_msgs.msg.ColorRGBA]: ...
    @colors.setter
    def colors(self, value: list[std_msgs.msg.ColorRGBA]) -> None: ...
    @property
    def texture_resource(self) -> str: ...
    @texture_resource.setter
    def texture_resource(self, value: str) -> None: ...
    @property
    def texture(self) -> sensor_msgs.msg.CompressedImage: ...
    @texture.setter
    def texture(self, value: sensor_msgs.msg.CompressedImage) -> None: ...
    @property
    def uv_coordinates(self) -> list[visualization_msgs.msg.UVCoordinate]: ...
    @uv_coordinates.setter
    def uv_coordinates(
        self, value: list[visualization_msgs.msg.UVCoordinate]
    ) -> None: ...
    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...
    @property
    def mesh_resource(self) -> str: ...
    @mesh_resource.setter
    def mesh_resource(self, value: str) -> None: ...
    @property
    def mesh_file(self) -> visualization_msgs.msg.MeshFile: ...
    @mesh_file.setter
    def mesh_file(self, value: visualization_msgs.msg.MeshFile) -> None: ...
    @property
    def mesh_use_embedded_materials(self) -> bool: ...
    @mesh_use_embedded_materials.setter
    def mesh_use_embedded_materials(self, value: bool) -> None: ...
