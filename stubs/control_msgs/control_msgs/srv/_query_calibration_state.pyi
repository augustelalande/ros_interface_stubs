# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

class QueryCalibrationState_Request:
    def __init__(
        self,
        *,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

class QueryCalibrationState_Response:
    def __init__(
        self,
        *,
        is_calibrated: bool = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...
    # Members
    @property
    def is_calibrated(self) -> bool: ...
    @is_calibrated.setter
    def is_calibrated(self, value: bool) -> None: ...

class QueryCalibrationState:
    Request: TypeAlias = QueryCalibrationState_Request
    Response: TypeAlias = QueryCalibrationState_Response
