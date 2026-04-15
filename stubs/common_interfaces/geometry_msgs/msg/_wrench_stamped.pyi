# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class WrenchStamped:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        wrench: geometry_msgs.msg.Wrench = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def wrench(self) -> geometry_msgs.msg.Wrench: ...
    @wrench.setter
    def wrench(self, value: geometry_msgs.msg.Wrench) -> None: ...
