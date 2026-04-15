# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class Transition:
    # Constants
    TRANSITION_CREATE: int = 0
    TRANSITION_CONFIGURE: int = 1
    TRANSITION_CLEANUP: int = 2
    TRANSITION_ACTIVATE: int = 3
    TRANSITION_DEACTIVATE: int = 4
    TRANSITION_UNCONFIGURED_SHUTDOWN: int = 5
    TRANSITION_INACTIVE_SHUTDOWN: int = 6
    TRANSITION_ACTIVE_SHUTDOWN: int = 7
    TRANSITION_DESTROY: int = 8
    TRANSITION_ON_CONFIGURE_SUCCESS: int = 10
    TRANSITION_ON_CONFIGURE_FAILURE: int = 11
    TRANSITION_ON_CONFIGURE_ERROR: int = 12
    TRANSITION_ON_CLEANUP_SUCCESS: int = 20
    TRANSITION_ON_CLEANUP_FAILURE: int = 21
    TRANSITION_ON_CLEANUP_ERROR: int = 22
    TRANSITION_ON_ACTIVATE_SUCCESS: int = 30
    TRANSITION_ON_ACTIVATE_FAILURE: int = 31
    TRANSITION_ON_ACTIVATE_ERROR: int = 32
    TRANSITION_ON_DEACTIVATE_SUCCESS: int = 40
    TRANSITION_ON_DEACTIVATE_FAILURE: int = 41
    TRANSITION_ON_DEACTIVATE_ERROR: int = 42
    TRANSITION_ON_SHUTDOWN_SUCCESS: int = 50
    TRANSITION_ON_SHUTDOWN_FAILURE: int = 51
    TRANSITION_ON_SHUTDOWN_ERROR: int = 52
    TRANSITION_ON_ERROR_SUCCESS: int = 60
    TRANSITION_ON_ERROR_FAILURE: int = 61
    TRANSITION_ON_ERROR_ERROR: int = 62
    TRANSITION_CALLBACK_SUCCESS: int = 97
    TRANSITION_CALLBACK_FAILURE: int = 98
    TRANSITION_CALLBACK_ERROR: int = 99

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
