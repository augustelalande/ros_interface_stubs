# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg

class ServiceEventInfo:
    # Constants
    REQUEST_SENT: int = 0
    REQUEST_RECEIVED: int = 1
    RESPONSE_SENT: int = 2
    RESPONSE_RECEIVED: int = 3

    def __init__(
        self,
        *,
        event_type: int = ...,
        stamp: builtin_interfaces.msg.Time = ...,
        client_gid: list[str] = ...,
        sequence_number: int = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def event_type(self) -> int: ...
    @event_type.setter
    def event_type(self, value: int) -> None: ...
    @property
    def stamp(self) -> builtin_interfaces.msg.Time: ...
    @stamp.setter
    def stamp(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def client_gid(self) -> list[str]: ...
    @client_gid.setter
    def client_gid(self, value: list[str]) -> None: ...
    @property
    def sequence_number(self) -> int: ...
    @sequence_number.setter
    def sequence_number(self, value: int) -> None: ...
