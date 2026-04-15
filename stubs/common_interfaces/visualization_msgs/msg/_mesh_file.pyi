# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class MeshFile:
    def __init__(
        self,
        *,
        filename: str = ...,
        data: list[int] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def filename(self) -> str: ...
    @filename.setter
    def filename(self, value: str) -> None: ...
    @property
    def data(self) -> list[int]: ...
    @data.setter
    def data(self, value: list[int]) -> None: ...
