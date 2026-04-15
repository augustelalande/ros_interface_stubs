# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import rosgraph_msgs.msg

class InterfaceType:
    def __init__(
        self,
        *,
        name: str = ...,
        hash: rosgraph_msgs.msg.TypeHash = ...,  # noqa: A002
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def hash(self) -> rosgraph_msgs.msg.TypeHash: ...
    @hash.setter
    def hash(self, value: rosgraph_msgs.msg.TypeHash) -> None: ...
