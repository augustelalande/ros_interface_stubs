# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class VDA5050State:
    # Constants
    ACTION_WAITING: str = "WAITING"
    ACTION_INITIALIZING: str = "INITIALIZING"
    ACTION_RUNNING: str = "RUNNING"
    ACTION_PAUSED: str = "PAUSED"
    ACTION_FINISHED: str = "FINISHED"
    ACTION_FAILED: str = "FAILED"
    MODE_AUTOMATIC: str = "AUTOMATIC"
    MODE_SEMI_AUTOMATIC: str = "SEMIAUTOMATIC"
    MODE_MANUAL: str = "MANUAL"
    MODE_SERVICE: str = "SERVICE"
    MODE_EMERGENCY: str = "EMERGENCY"
    MODE_TEACHIN: str = "TEACHIN"

    def __init__(
        self,
        *,
        order_id: str = ...,
        action_status: str = ...,
        last_node_id: int = ...,
        driving: bool = ...,
        battery_charge: float = ...,
        operating_mode: str = ...,
        error_type: str = ...,
        error_description: str = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def order_id(self) -> str: ...
    @order_id.setter
    def order_id(self, value: str) -> None: ...
    @property
    def action_status(self) -> str: ...
    @action_status.setter
    def action_status(self, value: str) -> None: ...
    @property
    def last_node_id(self) -> int: ...
    @last_node_id.setter
    def last_node_id(self, value: int) -> None: ...
    @property
    def driving(self) -> bool: ...
    @driving.setter
    def driving(self, value: bool) -> None: ...
    @property
    def battery_charge(self) -> float: ...
    @battery_charge.setter
    def battery_charge(self, value: float) -> None: ...
    @property
    def operating_mode(self) -> str: ...
    @operating_mode.setter
    def operating_mode(self, value: str) -> None: ...
    @property
    def error_type(self) -> str: ...
    @error_type.setter
    def error_type(self, value: str) -> None: ...
    @property
    def error_description(self) -> str: ...
    @error_description.setter
    def error_description(self, value: str) -> None: ...
