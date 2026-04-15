# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class EtherCATState:
    # Constants
    AL_STATE_INIT: int = 1
    AL_STATE_PREOP: int = 2
    AL_STATE_BOOTSTRAP: int = 3
    AL_STATE_SAFEOP: int = 4
    AL_STATE_OP: int = 8

    def __init__(
        self,
        *,
        slave_position: int = ...,
        vendor_id: str = ...,
        product_code: str = ...,
        al_state: int = ...,
        has_error: bool = ...,
        al_status_code: int = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def slave_position(self) -> int: ...
    @slave_position.setter
    def slave_position(self, value: int) -> None: ...
    @property
    def vendor_id(self) -> str: ...
    @vendor_id.setter
    def vendor_id(self, value: str) -> None: ...
    @property
    def product_code(self) -> str: ...
    @product_code.setter
    def product_code(self, value: str) -> None: ...
    @property
    def al_state(self) -> int: ...
    @al_state.setter
    def al_state(self, value: int) -> None: ...
    @property
    def has_error(self) -> bool: ...
    @has_error.setter
    def has_error(self, value: bool) -> None: ...
    @property
    def al_status_code(self) -> int: ...
    @al_status_code.setter
    def al_status_code(self, value: int) -> None: ...
