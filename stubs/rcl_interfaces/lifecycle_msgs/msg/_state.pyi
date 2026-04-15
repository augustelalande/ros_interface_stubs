# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class State:
    # Constants
    PRIMARY_STATE_UNKNOWN: int = 0
    PRIMARY_STATE_UNCONFIGURED: int = 1
    PRIMARY_STATE_INACTIVE: int = 2
    PRIMARY_STATE_ACTIVE: int = 3
    PRIMARY_STATE_FINALIZED: int = 4
    TRANSITION_STATE_CONFIGURING: int = 10
    TRANSITION_STATE_CLEANINGUP: int = 11
    TRANSITION_STATE_SHUTTINGDOWN: int = 12
    TRANSITION_STATE_ACTIVATING: int = 13
    TRANSITION_STATE_DEACTIVATING: int = 14
    TRANSITION_STATE_ERRORPROCESSING: int = 15

    def __init__(
        self,
        *,
        id: int = ...,  # noqa: A002
        label: str = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, value: int) -> None: ...
    @property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str) -> None: ...
