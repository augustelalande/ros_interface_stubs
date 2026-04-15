# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import visualization_msgs.msg

class InteractiveMarkerUpdate:
    # Constants
    KEEP_ALIVE: int = 0
    UPDATE: int = 1

    def __init__(
        self,
        *,
        server_id: str = ...,
        seq_num: int = ...,
        type: int = ...,  # noqa: A002
        markers: list[visualization_msgs.msg.InteractiveMarker] = ...,
        poses: list[visualization_msgs.msg.InteractiveMarkerPose] = ...,
        erases: list[str] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def server_id(self) -> str: ...
    @server_id.setter
    def server_id(self, value: str) -> None: ...
    @property
    def seq_num(self) -> int: ...
    @seq_num.setter
    def seq_num(self, value: int) -> None: ...
    @property
    def type(self) -> int: ...
    @type.setter
    def type(self, value: int) -> None: ...
    @property
    def markers(self) -> list[visualization_msgs.msg.InteractiveMarker]: ...
    @markers.setter
    def markers(
        self, value: list[visualization_msgs.msg.InteractiveMarker]
    ) -> None: ...
    @property
    def poses(self) -> list[visualization_msgs.msg.InteractiveMarkerPose]: ...
    @poses.setter
    def poses(
        self, value: list[visualization_msgs.msg.InteractiveMarkerPose]
    ) -> None: ...
    @property
    def erases(self) -> list[str]: ...
    @erases.setter
    def erases(self, value: list[str]) -> None: ...
