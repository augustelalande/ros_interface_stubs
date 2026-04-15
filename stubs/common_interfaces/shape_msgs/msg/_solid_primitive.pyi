# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class SolidPrimitive:
    # Constants
    BOX: int = 1
    SPHERE: int = 2
    CYLINDER: int = 3
    CONE: int = 4
    PRISM: int = 5
    BOX_X: int = 0
    BOX_Y: int = 1
    BOX_Z: int = 2
    SPHERE_RADIUS: int = 0
    CYLINDER_HEIGHT: int = 0
    CYLINDER_RADIUS: int = 1
    CONE_HEIGHT: int = 0
    CONE_RADIUS: int = 1
    PRISM_HEIGHT: int = 0

    def __init__(
        self,
        *,
        type: int = ...,  # noqa: A002
        dimensions: list[float] = ...,
        polygon: geometry_msgs.msg.Polygon = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def type(self) -> int: ...
    @type.setter
    def type(self, value: int) -> None: ...
    @property
    def dimensions(self) -> list[float]: ...
    @dimensions.setter
    def dimensions(self, value: list[float]) -> None: ...
    @property
    def polygon(self) -> geometry_msgs.msg.Polygon: ...
    @polygon.setter
    def polygon(self, value: geometry_msgs.msg.Polygon) -> None: ...
