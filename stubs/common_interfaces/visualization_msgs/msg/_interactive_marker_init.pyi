# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import visualization_msgs.msg

class InteractiveMarkerInit:
    def __init__(
        self,
        *,
        server_id: str = ...,
        seq_num: int = ...,
        markers: list[visualization_msgs.msg.InteractiveMarker] = ...,
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
    def markers(self) -> list[visualization_msgs.msg.InteractiveMarker]: ...
    @markers.setter
    def markers(
        self, value: list[visualization_msgs.msg.InteractiveMarker]
    ) -> None: ...
