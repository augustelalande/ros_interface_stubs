# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class InertiaStamped:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        inertia: geometry_msgs.msg.Inertia = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def inertia(self) -> geometry_msgs.msg.Inertia: ...
    @inertia.setter
    def inertia(self, value: geometry_msgs.msg.Inertia) -> None: ...
