# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import sensor_msgs.msg

class SetCameraInfo_Request:
    def __init__(
        self,
        *,
        camera_info: sensor_msgs.msg.CameraInfo = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def camera_info(self) -> sensor_msgs.msg.CameraInfo: ...
    @camera_info.setter
    def camera_info(self, value: sensor_msgs.msg.CameraInfo) -> None: ...

class SetCameraInfo_Response:
    def __init__(
        self,
        *,
        success: bool = ...,
        status_message: str = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...
    @property
    def status_message(self) -> str: ...
    @status_message.setter
    def status_message(self, value: str) -> None: ...

class SetCameraInfo:
    Request: TypeAlias = SetCameraInfo_Request
    Response: TypeAlias = SetCameraInfo_Response
