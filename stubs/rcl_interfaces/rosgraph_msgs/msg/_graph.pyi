# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import rosgraph_msgs.msg

class Graph:
    def __init__(
        self,
        *,
        nodes: list[rosgraph_msgs.msg.Node] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def nodes(self) -> list[rosgraph_msgs.msg.Node]: ...
    @nodes.setter
    def nodes(self, value: list[rosgraph_msgs.msg.Node]) -> None: ...
