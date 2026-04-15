# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sensor_msgs.msg

class BatteryStateArray:
    def __init__(
        self,
        *,
        battery_states: list[sensor_msgs.msg.BatteryState] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def battery_states(self) -> list[sensor_msgs.msg.BatteryState]: ...
    @battery_states.setter
    def battery_states(self, value: list[sensor_msgs.msg.BatteryState]) -> None: ...
