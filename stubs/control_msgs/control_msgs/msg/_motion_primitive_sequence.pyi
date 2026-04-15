# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg

class MotionPrimitiveSequence:
    def __init__(
        self,
        *,
        motions: list[control_msgs.msg.MotionPrimitive] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def motions(self) -> list[control_msgs.msg.MotionPrimitive]: ...
    @motions.setter
    def motions(self, value: list[control_msgs.msg.MotionPrimitive]) -> None: ...
