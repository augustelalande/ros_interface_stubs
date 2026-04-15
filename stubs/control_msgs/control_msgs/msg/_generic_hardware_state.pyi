# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import diagnostic_msgs.msg

class GenericHardwareState:
    # Constants
    HEALTH_UNKNOWN: int = 0
    HEALTH_OK: int = 1
    HEALTH_DEGRADED: int = 2
    HEALTH_WARNING: int = 3
    HEALTH_ERROR: int = 4
    HEALTH_FATAL: int = 5
    ERROR_NONE: int = 0
    ERROR_UNKNOWN: int = 1
    ERROR_HW: int = 2
    ERROR_SW: int = 3
    ERROR_OVER_TRAVEL: int = 4
    EMERGENCY_STOP_HW: int = 5
    EMERGENCY_STOP_SW: int = 6
    PROTECTIVE_STOP_HW: int = 7
    PROTECTIVE_STOP_SW: int = 8
    SAFETY_STOP: int = 9
    CALIBRATION_REQUIRED: int = 10
    MODE_UNKNOWN: int = 0
    MODE_MANUAL: int = 1
    MODE_AUTO: int = 2
    MODE_SAFE: int = 3
    MODE_MAINTENANCE: int = 4
    MODE_JOG_MANUAL: int = 5
    MODE_ADMITTANCE: int = 6
    MODE_MONITORED_STOP: int = 7
    MODE_HOLD_TO_RUN: int = 8
    MODE_CARTESIAN_TWIST: int = 9
    MODE_CARTESIAN_POSE: int = 10
    MODE_TRAJECTORY_FORWARDING: int = 11
    MODE_TRAJECTORY_STREAMING: int = 12
    POWER_UNKNOWN: int = 0
    POWER_OFF: int = 1
    POWER_STANDBY: int = 2
    POWER_ON: int = 3
    POWER_SLEEP: int = 4
    POWER_ERROR: int = 5
    POWER_LEVEL_LOW: int = 6
    POWER_LEVEL_CRITICAL: int = 7
    POWER_CHARGING: int = 8
    POWER_CHARGING_ERROR: int = 9
    CONNECT_UNKNOWN: int = 0
    CONNECT_UP: int = 1
    CONNECT_DOWN: int = 2
    CONNECT_FAILURE: int = 3
    CONNECTION_SLOW: int = 4

    def __init__(
        self,
        *,
        health_status: int = ...,
        error_domain: list[int] = ...,
        operational_mode: int = ...,
        power_state: int = ...,
        connectivity_status: int = ...,
        manufacturer: str = ...,
        model: str = ...,
        firmware_version: str = ...,
        state_details: list[diagnostic_msgs.msg.KeyValue] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def health_status(self) -> int: ...
    @health_status.setter
    def health_status(self, value: int) -> None: ...
    @property
    def error_domain(self) -> list[int]: ...
    @error_domain.setter
    def error_domain(self, value: list[int]) -> None: ...
    @property
    def operational_mode(self) -> int: ...
    @operational_mode.setter
    def operational_mode(self, value: int) -> None: ...
    @property
    def power_state(self) -> int: ...
    @power_state.setter
    def power_state(self, value: int) -> None: ...
    @property
    def connectivity_status(self) -> int: ...
    @connectivity_status.setter
    def connectivity_status(self, value: int) -> None: ...
    @property
    def manufacturer(self) -> str: ...
    @manufacturer.setter
    def manufacturer(self, value: str) -> None: ...
    @property
    def model(self) -> str: ...
    @model.setter
    def model(self, value: str) -> None: ...
    @property
    def firmware_version(self) -> str: ...
    @firmware_version.setter
    def firmware_version(self, value: str) -> None: ...
    @property
    def state_details(self) -> list[diagnostic_msgs.msg.KeyValue]: ...
    @state_details.setter
    def state_details(self, value: list[diagnostic_msgs.msg.KeyValue]) -> None: ...
