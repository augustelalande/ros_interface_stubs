# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import control_msgs.msg
import std_msgs.msg

class HardwareDiagnostics:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        hardware_id: str = ...,
        hardware_device_diagnostics: list[
            control_msgs.msg.HardwareDeviceDiagnostics
        ] = ...,
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
    def hardware_id(self) -> str: ...
    @hardware_id.setter
    def hardware_id(self, value: str) -> None: ...
    @property
    def hardware_device_diagnostics(
        self,
    ) -> list[control_msgs.msg.HardwareDeviceDiagnostics]: ...
    @hardware_device_diagnostics.setter
    def hardware_device_diagnostics(
        self, value: list[control_msgs.msg.HardwareDeviceDiagnostics]
    ) -> None: ...
