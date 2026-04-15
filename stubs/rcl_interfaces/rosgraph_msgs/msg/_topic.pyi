# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import rosgraph_msgs.msg

class Topic:
    def __init__(
        self,
        *,
        name: str = ...,
        type: rosgraph_msgs.msg.InterfaceType = ...,  # noqa: A002
        qos: rosgraph_msgs.msg.QoSProfile = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def type(self) -> rosgraph_msgs.msg.InterfaceType: ...
    @type.setter
    def type(self, value: rosgraph_msgs.msg.InterfaceType) -> None: ...
    @property
    def qos(self) -> rosgraph_msgs.msg.QoSProfile: ...
    @qos.setter
    def qos(self, value: rosgraph_msgs.msg.QoSProfile) -> None: ...
