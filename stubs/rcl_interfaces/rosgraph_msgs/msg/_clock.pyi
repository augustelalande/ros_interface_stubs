# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg

class Clock:
    def __init__(
        self,
        *,
        clock: builtin_interfaces.msg.Time = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def clock(self) -> builtin_interfaces.msg.Time: ...
    @clock.setter
    def clock(self, value: builtin_interfaces.msg.Time) -> None: ...
