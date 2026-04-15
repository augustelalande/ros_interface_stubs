# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg

class BatteryState:
    # Constants
    POWER_SUPPLY_STATUS_UNKNOWN: int = 0
    POWER_SUPPLY_STATUS_CHARGING: int = 1
    POWER_SUPPLY_STATUS_DISCHARGING: int = 2
    POWER_SUPPLY_STATUS_NOT_CHARGING: int = 3
    POWER_SUPPLY_STATUS_FULL: int = 4
    POWER_SUPPLY_HEALTH_UNKNOWN: int = 0
    POWER_SUPPLY_HEALTH_GOOD: int = 1
    POWER_SUPPLY_HEALTH_OVERHEAT: int = 2
    POWER_SUPPLY_HEALTH_DEAD: int = 3
    POWER_SUPPLY_HEALTH_OVERVOLTAGE: int = 4
    POWER_SUPPLY_HEALTH_UNSPEC_FAILURE: int = 5
    POWER_SUPPLY_HEALTH_COLD: int = 6
    POWER_SUPPLY_HEALTH_WATCHDOG_TIMER_EXPIRE: int = 7
    POWER_SUPPLY_HEALTH_SAFETY_TIMER_EXPIRE: int = 8
    POWER_SUPPLY_TECHNOLOGY_UNKNOWN: int = 0
    POWER_SUPPLY_TECHNOLOGY_NIMH: int = 1
    POWER_SUPPLY_TECHNOLOGY_LION: int = 2
    POWER_SUPPLY_TECHNOLOGY_LIPO: int = 3
    POWER_SUPPLY_TECHNOLOGY_LIFE: int = 4
    POWER_SUPPLY_TECHNOLOGY_NICD: int = 5
    POWER_SUPPLY_TECHNOLOGY_LIMN: int = 6
    POWER_SUPPLY_TECHNOLOGY_TERNARY: int = 7
    POWER_SUPPLY_TECHNOLOGY_VRLA: int = 8

    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        voltage: float = ...,
        temperature: float = ...,
        current: float = ...,
        charge: float = ...,
        capacity: float = ...,
        design_capacity: float = ...,
        percentage: float = ...,
        power_supply_status: int = ...,
        power_supply_health: int = ...,
        power_supply_technology: int = ...,
        present: bool = ...,
        cell_voltage: list[float] = ...,
        cell_temperature: list[float] = ...,
        location: str = ...,
        serial_number: str = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def voltage(self) -> float: ...
    @voltage.setter
    def voltage(self, value: float) -> None: ...
    @property
    def temperature(self) -> float: ...
    @temperature.setter
    def temperature(self, value: float) -> None: ...
    @property
    def current(self) -> float: ...
    @current.setter
    def current(self, value: float) -> None: ...
    @property
    def charge(self) -> float: ...
    @charge.setter
    def charge(self, value: float) -> None: ...
    @property
    def capacity(self) -> float: ...
    @capacity.setter
    def capacity(self, value: float) -> None: ...
    @property
    def design_capacity(self) -> float: ...
    @design_capacity.setter
    def design_capacity(self, value: float) -> None: ...
    @property
    def percentage(self) -> float: ...
    @percentage.setter
    def percentage(self, value: float) -> None: ...
    @property
    def power_supply_status(self) -> int: ...
    @power_supply_status.setter
    def power_supply_status(self, value: int) -> None: ...
    @property
    def power_supply_health(self) -> int: ...
    @power_supply_health.setter
    def power_supply_health(self, value: int) -> None: ...
    @property
    def power_supply_technology(self) -> int: ...
    @power_supply_technology.setter
    def power_supply_technology(self, value: int) -> None: ...
    @property
    def present(self) -> bool: ...
    @present.setter
    def present(self, value: bool) -> None: ...
    @property
    def cell_voltage(self) -> list[float]: ...
    @cell_voltage.setter
    def cell_voltage(self, value: list[float]) -> None: ...
    @property
    def cell_temperature(self) -> list[float]: ...
    @cell_temperature.setter
    def cell_temperature(self, value: list[float]) -> None: ...
    @property
    def location(self) -> str: ...
    @location.setter
    def location(self, value: str) -> None: ...
    @property
    def serial_number(self) -> str: ...
    @serial_number.setter
    def serial_number(self, value: str) -> None: ...
