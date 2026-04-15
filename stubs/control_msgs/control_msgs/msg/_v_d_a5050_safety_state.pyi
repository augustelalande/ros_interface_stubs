# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class VDA5050SafetyState:
    # Constants
    AUTO_ACK: str = "autoAck"
    MANUAL: str = "manual"
    REMOTE: str = "remote"
    NONE: str = "none"

    def __init__(
        self,
        *,
        e_stop: str = ...,
        field_violation: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def e_stop(self) -> str: ...
    @e_stop.setter
    def e_stop(self, value: str) -> None: ...
    @property
    def field_violation(self) -> bool: ...
    @field_violation.setter
    def field_violation(self, value: bool) -> None: ...
