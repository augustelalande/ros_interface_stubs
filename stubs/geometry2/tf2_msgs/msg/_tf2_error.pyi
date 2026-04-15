# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class TF2Error:
    # Constants
    NO_ERROR: int = 0
    LOOKUP_ERROR: int = 1
    CONNECTIVITY_ERROR: int = 2
    EXTRAPOLATION_ERROR: int = 3
    INVALID_ARGUMENT_ERROR: int = 4
    TIMEOUT_ERROR: int = 5
    TRANSFORM_ERROR: int = 6

    def __init__(
        self,
        *,
        error: int = ...,
        error_string: str = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def error(self) -> int: ...
    @error.setter
    def error(self, value: int) -> None: ...
    @property
    def error_string(self) -> str: ...
    @error_string.setter
    def error_string(self, value: str) -> None: ...
