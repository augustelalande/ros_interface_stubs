# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class Vector3Stamped:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        vector: geometry_msgs.msg.Vector3 = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def vector(self) -> geometry_msgs.msg.Vector3: ...
    @vector.setter
    def vector(self, value: geometry_msgs.msg.Vector3) -> None: ...
