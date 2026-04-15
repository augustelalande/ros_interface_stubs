# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class TransformStamped:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        child_frame_id: str = ...,
        transform: geometry_msgs.msg.Transform = ...,
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
    def child_frame_id(self) -> str: ...
    @child_frame_id.setter
    def child_frame_id(self, value: str) -> None: ...
    @property
    def transform(self) -> geometry_msgs.msg.Transform: ...
    @transform.setter
    def transform(self, value: geometry_msgs.msg.Transform) -> None: ...
