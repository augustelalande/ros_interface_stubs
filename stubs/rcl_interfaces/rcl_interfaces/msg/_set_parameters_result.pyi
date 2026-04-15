# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class SetParametersResult:
    def __init__(
        self,
        *,
        successful: bool = ...,
        reason: str = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def successful(self) -> bool: ...
    @successful.setter
    def successful(self, value: bool) -> None: ...
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str) -> None: ...
