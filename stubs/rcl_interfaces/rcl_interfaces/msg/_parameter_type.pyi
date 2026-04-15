# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class ParameterType:
    # Constants
    PARAMETER_NOT_SET: int = 0
    PARAMETER_BOOL: int = 1
    PARAMETER_INTEGER: int = 2
    PARAMETER_DOUBLE: int = 3
    PARAMETER_STRING: int = 4
    PARAMETER_BYTE_ARRAY: int = 5
    PARAMETER_BOOL_ARRAY: int = 6
    PARAMETER_INTEGER_ARRAY: int = 7
    PARAMETER_DOUBLE_ARRAY: int = 8
    PARAMETER_STRING_ARRAY: int = 9

    def __init__(
        self,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
