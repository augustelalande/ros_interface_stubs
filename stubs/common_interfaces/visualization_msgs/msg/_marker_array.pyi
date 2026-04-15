# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import visualization_msgs.msg

class MarkerArray:
    def __init__(
        self,
        *,
        markers: list[visualization_msgs.msg.Marker] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def markers(self) -> list[visualization_msgs.msg.Marker]: ...
    @markers.setter
    def markers(self, value: list[visualization_msgs.msg.Marker]) -> None: ...
