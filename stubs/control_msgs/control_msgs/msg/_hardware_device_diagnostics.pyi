# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import diagnostic_msgs.msg
import std_msgs.msg

class HardwareDeviceDiagnostics:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        device_id: str = ...,
        entries: list[diagnostic_msgs.msg.KeyValue] = ...,
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
    def entries(self) -> list[diagnostic_msgs.msg.KeyValue]: ...
    @entries.setter
    def entries(self, value: list[diagnostic_msgs.msg.KeyValue]) -> None: ...
