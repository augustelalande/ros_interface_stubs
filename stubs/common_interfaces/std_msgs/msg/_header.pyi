# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg

class Header:
    def __init__(
        self,
        *,
        stamp: builtin_interfaces.msg.Time = ...,
        frame_id: str = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def stamp(self) -> builtin_interfaces.msg.Time: ...
    @stamp.setter
    def stamp(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def frame_id(self) -> str: ...
    @frame_id.setter
    def frame_id(self, value: str) -> None: ...
