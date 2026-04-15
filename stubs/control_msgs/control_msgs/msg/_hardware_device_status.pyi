# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg
import std_msgs.msg

class HardwareDeviceStatus:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        device_id: str = ...,
        hardware_status: list[control_msgs.msg.GenericHardwareState] = ...,
        canopen_states: list[control_msgs.msg.CANopenState] = ...,
        ethercat_states: list[control_msgs.msg.EtherCATState] = ...,
        vda5050_states: list[control_msgs.msg.VDA5050State] = ...,
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
    def device_id(self) -> str: ...
    @device_id.setter
    def device_id(self, value: str) -> None: ...
    @property
    def hardware_status(self) -> list[control_msgs.msg.GenericHardwareState]: ...
    @hardware_status.setter
    def hardware_status(
        self, value: list[control_msgs.msg.GenericHardwareState]
    ) -> None: ...
    @property
    def canopen_states(self) -> list[control_msgs.msg.CANopenState]: ...
    @canopen_states.setter
    def canopen_states(self, value: list[control_msgs.msg.CANopenState]) -> None: ...
    @property
    def ethercat_states(self) -> list[control_msgs.msg.EtherCATState]: ...
    @ethercat_states.setter
    def ethercat_states(self, value: list[control_msgs.msg.EtherCATState]) -> None: ...
    @property
    def vda5050_states(self) -> list[control_msgs.msg.VDA5050State]: ...
    @vda5050_states.setter
    def vda5050_states(self, value: list[control_msgs.msg.VDA5050State]) -> None: ...
