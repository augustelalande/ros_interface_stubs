# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

class FrameGraph_Request:
    def __init__(
        self,
        *,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class FrameGraph_Response:
    def __init__(
        self,
        *,
        frame_yaml: str = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def frame_yaml(self) -> str: ...
    @frame_yaml.setter
    def frame_yaml(self, value: str) -> None: ...

class FrameGraph:
    Request: TypeAlias = FrameGraph_Request
    Response: TypeAlias = FrameGraph_Response
