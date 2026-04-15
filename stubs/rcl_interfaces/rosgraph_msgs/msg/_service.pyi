# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import rosgraph_msgs.msg

class Service:
    def __init__(
        self,
        *,
        name: str = ...,
        request_type: rosgraph_msgs.msg.InterfaceType = ...,
        request_qos: rosgraph_msgs.msg.QoSProfile = ...,
        response_type: rosgraph_msgs.msg.InterfaceType = ...,
        response_qos: rosgraph_msgs.msg.QoSProfile = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def request_type(self) -> rosgraph_msgs.msg.InterfaceType: ...
    @request_type.setter
    def request_type(self, value: rosgraph_msgs.msg.InterfaceType) -> None: ...
    @property
    def request_qos(self) -> rosgraph_msgs.msg.QoSProfile: ...
    @request_qos.setter
    def request_qos(self, value: rosgraph_msgs.msg.QoSProfile) -> None: ...
    @property
    def response_type(self) -> rosgraph_msgs.msg.InterfaceType: ...
    @response_type.setter
    def response_type(self, value: rosgraph_msgs.msg.InterfaceType) -> None: ...
    @property
    def response_qos(self) -> rosgraph_msgs.msg.QoSProfile: ...
    @response_qos.setter
    def response_qos(self, value: rosgraph_msgs.msg.QoSProfile) -> None: ...
