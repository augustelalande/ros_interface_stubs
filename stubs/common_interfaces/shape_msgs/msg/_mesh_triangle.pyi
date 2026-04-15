# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class MeshTriangle:
    def __init__(
        self,
        *,
        vertex_indices: list[int] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def vertex_indices(self) -> list[int]: ...
    @vertex_indices.setter
    def vertex_indices(self, value: list[int]) -> None: ...
