# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg
import std_msgs.msg

class MultiDOFJointState:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        joint_names: list[str] = ...,
        transforms: list[geometry_msgs.msg.Transform] = ...,
        twist: list[geometry_msgs.msg.Twist] = ...,
        wrench: list[geometry_msgs.msg.Wrench] = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def header(self) -> std_msgs.msg.Header: ...
    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None: ...
    @property
    def joint_names(self) -> list[str]: ...
    @joint_names.setter
    def joint_names(self, value: list[str]) -> None: ...
    @property
    def transforms(self) -> list[geometry_msgs.msg.Transform]: ...
    @transforms.setter
    def transforms(self, value: list[geometry_msgs.msg.Transform]) -> None: ...
    @property
    def twist(self) -> list[geometry_msgs.msg.Twist]: ...
    @twist.setter
    def twist(self, value: list[geometry_msgs.msg.Twist]) -> None: ...
    @property
    def wrench(self) -> list[geometry_msgs.msg.Wrench]: ...
    @wrench.setter
    def wrench(self, value: list[geometry_msgs.msg.Wrench]) -> None: ...
