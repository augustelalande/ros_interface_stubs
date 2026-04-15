# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class LoggerLevel:
    # Constants
    LOG_LEVEL_UNKNOWN: int = 0
    LOG_LEVEL_DEBUG: int = 10
    LOG_LEVEL_INFO: int = 20
    LOG_LEVEL_WARN: int = 30
    LOG_LEVEL_ERROR: int = 40
    LOG_LEVEL_FATAL: int = 50

    def __init__(
        self, *, name: str = ..., level: int = ..., check_fields: bool = ...
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def level(self) -> int: ...
    @level.setter
    def level(self, value: int) -> None: ...
