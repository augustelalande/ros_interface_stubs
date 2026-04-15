# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import std_msgs.msg
import trajectory_msgs.msg

class JointTrajectoryControllerState:
    def __init__(
        self,
        *,
        header: std_msgs.msg.Header = ...,
        joint_names: list[str] = ...,
        reference: trajectory_msgs.msg.JointTrajectoryPoint = ...,
        feedback: trajectory_msgs.msg.JointTrajectoryPoint = ...,
        error: trajectory_msgs.msg.JointTrajectoryPoint = ...,
        output: trajectory_msgs.msg.JointTrajectoryPoint = ...,
        multi_dof_joint_names: list[str] = ...,
        multi_dof_reference: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint = ...,
        multi_dof_feedback: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint = ...,
        multi_dof_error: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint = ...,
        multi_dof_output: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint = ...,
        speed_scaling_factor: float = ...,
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
    def reference(self) -> trajectory_msgs.msg.JointTrajectoryPoint: ...
    @reference.setter
    def reference(self, value: trajectory_msgs.msg.JointTrajectoryPoint) -> None: ...
    @property
    def feedback(self) -> trajectory_msgs.msg.JointTrajectoryPoint: ...
    @feedback.setter
    def feedback(self, value: trajectory_msgs.msg.JointTrajectoryPoint) -> None: ...
    @property
    def error(self) -> trajectory_msgs.msg.JointTrajectoryPoint: ...
    @error.setter
    def error(self, value: trajectory_msgs.msg.JointTrajectoryPoint) -> None: ...
    @property
    def output(self) -> trajectory_msgs.msg.JointTrajectoryPoint: ...
    @output.setter
    def output(self, value: trajectory_msgs.msg.JointTrajectoryPoint) -> None: ...
    @property
    def multi_dof_joint_names(self) -> list[str]: ...
    @multi_dof_joint_names.setter
    def multi_dof_joint_names(self, value: list[str]) -> None: ...
    @property
    def multi_dof_reference(
        self,
    ) -> trajectory_msgs.msg.MultiDOFJointTrajectoryPoint: ...
    @multi_dof_reference.setter
    def multi_dof_reference(
        self, value: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint
    ) -> None: ...
    @property
    def multi_dof_feedback(
        self,
    ) -> trajectory_msgs.msg.MultiDOFJointTrajectoryPoint: ...
    @multi_dof_feedback.setter
    def multi_dof_feedback(
        self, value: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint
    ) -> None: ...
    @property
    def multi_dof_error(self) -> trajectory_msgs.msg.MultiDOFJointTrajectoryPoint: ...
    @multi_dof_error.setter
    def multi_dof_error(
        self, value: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint
    ) -> None: ...
    @property
    def multi_dof_output(self) -> trajectory_msgs.msg.MultiDOFJointTrajectoryPoint: ...
    @multi_dof_output.setter
    def multi_dof_output(
        self, value: trajectory_msgs.msg.MultiDOFJointTrajectoryPoint
    ) -> None: ...
    @property
    def speed_scaling_factor(self) -> float: ...
    @speed_scaling_factor.setter
    def speed_scaling_factor(self, value: float) -> None: ...
