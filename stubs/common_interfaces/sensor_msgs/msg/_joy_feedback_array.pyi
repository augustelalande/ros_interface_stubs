# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sensor_msgs.msg

class JoyFeedbackArray:
    def __init__(
        self,
        *,
        array: list[sensor_msgs.msg.JoyFeedback] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def array(self) -> list[sensor_msgs.msg.JoyFeedback]: ...
    @array.setter
    def array(self, value: list[sensor_msgs.msg.JoyFeedback]) -> None: ...
