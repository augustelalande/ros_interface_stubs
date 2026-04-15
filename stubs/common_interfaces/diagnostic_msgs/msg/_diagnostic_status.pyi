# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import diagnostic_msgs.msg

class DiagnosticStatus:
    # Constants
    OK: int = 0
    WARN: int = 1
    ERROR: int = 2
    STALE: int = 3

    def __init__(
        self,
        *,
        level: bytes = ...,
        name: str = ...,
        message: str = ...,
        hardware_id: str = ...,
        values: list[diagnostic_msgs.msg.KeyValue] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def level(self) -> bytes: ...
    @level.setter
    def level(self, value: bytes) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str) -> None: ...
    @property
    def hardware_id(self) -> str: ...
    @hardware_id.setter
    def hardware_id(self, value: str) -> None: ...
    @property
    def values(self) -> list[diagnostic_msgs.msg.KeyValue]: ...
    @values.setter
    def values(self, value: list[diagnostic_msgs.msg.KeyValue]) -> None: ...
