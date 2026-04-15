# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class WrenchFramed:
    def __init__(
        self,
        *,
        frame_id: str = ...,
        wrench: geometry_msgs.msg.Wrench = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def frame_id(self) -> str: ...
    @frame_id.setter
    def frame_id(self, value: str) -> None: ...
    @property
    def wrench(self) -> geometry_msgs.msg.Wrench: ...
    @wrench.setter
    def wrench(self, value: geometry_msgs.msg.Wrench) -> None: ...
