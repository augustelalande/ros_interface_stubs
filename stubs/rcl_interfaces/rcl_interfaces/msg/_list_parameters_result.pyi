# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class ListParametersResult:
    def __init__(
        self,
        *,
        names: list[str] = ...,
        prefixes: list[str] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def names(self) -> list[str]: ...
    @names.setter
    def names(self, value: list[str]) -> None: ...
    @property
    def prefixes(self) -> list[str]: ...
    @prefixes.setter
    def prefixes(self, value: list[str]) -> None: ...
