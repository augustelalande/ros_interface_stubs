# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

class ListNodes_Request:
    def __init__(
        self,
        *,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class ListNodes_Response:
    def __init__(
        self,
        *,
        full_node_names: list[str] = ...,
        unique_ids: list[int] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def full_node_names(self) -> list[str]: ...
    @full_node_names.setter
    def full_node_names(self, value: list[str]) -> None: ...
    @property
    def unique_ids(self) -> list[int]: ...
    @unique_ids.setter
    def unique_ids(self, value: list[int]) -> None: ...

class ListNodes:
    Request: TypeAlias = ListNodes_Request
    Response: TypeAlias = ListNodes_Response
