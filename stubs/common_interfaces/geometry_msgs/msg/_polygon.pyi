# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class Polygon:
    def __init__(
        self, *, points: list[geometry_msgs.msg.Point32] = ..., check_fields: bool = ...
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def points(self) -> list[geometry_msgs.msg.Point32]: ...
    @points.setter
    def points(self, value: list[geometry_msgs.msg.Point32]) -> None: ...
