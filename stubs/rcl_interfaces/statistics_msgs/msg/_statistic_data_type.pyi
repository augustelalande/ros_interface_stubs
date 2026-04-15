# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class StatisticDataType:
    # Constants
    STATISTICS_DATA_TYPE_UNINITIALIZED: int = 0
    STATISTICS_DATA_TYPE_AVERAGE: int = 1
    STATISTICS_DATA_TYPE_MINIMUM: int = 2
    STATISTICS_DATA_TYPE_MAXIMUM: int = 3
    STATISTICS_DATA_TYPE_STDDEV: int = 4
    STATISTICS_DATA_TYPE_SAMPLE_COUNT: int = 5

    def __init__(self, *, check_fields: bool = ...) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
