# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg

class Builtins:
    def __init__(
        self,
        *,
        duration_value: builtin_interfaces.msg.Duration = ...,
        time_value: builtin_interfaces.msg.Time = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def duration_value(self) -> builtin_interfaces.msg.Duration: ...
    @duration_value.setter
    def duration_value(self, value: builtin_interfaces.msg.Duration) -> None: ...
    @property
    def time_value(self) -> builtin_interfaces.msg.Time: ...
    @time_value.setter
    def time_value(self, value: builtin_interfaces.msg.Time) -> None: ...
