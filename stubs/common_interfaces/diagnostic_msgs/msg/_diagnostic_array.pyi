# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import diagnostic_msgs.msg
import std_msgs.msg

class DiagnosticArray:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        status: list[diagnostic_msgs.msg.DiagnosticStatus] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def status(self) -> list[diagnostic_msgs.msg.DiagnosticStatus]: ...
    @status.setter
    def status(self, value: list[diagnostic_msgs.msg.DiagnosticStatus]) -> None: ...
