# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg

class Log:
    # Constants
    DEBUG: int = 10
    INFO: int = 20
    WARN: int = 30
    ERROR: int = 40
    FATAL: int = 50

    def __init__(
        self,
        *,
        stamp: builtin_interfaces.msg.Time = ...,
        level: int = ...,
        name: str = ...,
        msg: str = ...,
        file: str = ...,
        function: str = ...,
        line: int = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def stamp(self) -> builtin_interfaces.msg.Time: ...
    @stamp.setter
    def stamp(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def level(self) -> int: ...
    @level.setter
    def level(self, value: int) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def msg(self) -> str: ...
    @msg.setter
    def msg(self, value: str) -> None: ...
    @property
    def file(self) -> str: ...
    @file.setter
    def file(self, value: str) -> None: ...
    @property
    def function(self) -> str: ...
    @function.setter
    def function(self, value: str) -> None: ...
    @property
    def line(self) -> int: ...
    @line.setter
    def line(self, value: int) -> None: ...
