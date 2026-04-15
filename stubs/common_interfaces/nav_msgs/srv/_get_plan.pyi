# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import geometry_msgs.msg
import nav_msgs.msg

class GetPlan_Request:
    def __init__(
        self,
        *,
        start: geometry_msgs.msg.PoseStamped = ...,
        goal: geometry_msgs.msg.PoseStamped = ...,
        tolerance: float = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def start(self) -> geometry_msgs.msg.PoseStamped: ...
    @start.setter
    def start(self, value: geometry_msgs.msg.PoseStamped) -> None: ...
    @property
    def goal(self) -> geometry_msgs.msg.PoseStamped: ...
    @goal.setter
    def goal(self, value: geometry_msgs.msg.PoseStamped) -> None: ...
    @property
    def tolerance(self) -> float: ...
    @tolerance.setter
    def tolerance(self, value: float) -> None: ...

class GetPlan_Response:
    def __init__(
        self,
        *,
        plan: nav_msgs.msg.Path = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def plan(self) -> nav_msgs.msg.Path: ...
    @plan.setter
    def plan(self, value: nav_msgs.msg.Path) -> None: ...

class GetPlan:
    Request: TypeAlias = GetPlan_Request
    Response: TypeAlias = GetPlan_Response
