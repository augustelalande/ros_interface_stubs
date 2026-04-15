# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class NavSatStatus:
    # Constants
    STATUS_UNKNOWN: int = -2
    STATUS_NO_FIX: int = -1
    STATUS_FIX: int = 0
    STATUS_SBAS_FIX: int = 1
    STATUS_GBAS_FIX: int = 2
    SERVICE_UNKNOWN: int = 0
    SERVICE_GPS: int = 1
    SERVICE_GLONASS: int = 2
    SERVICE_COMPASS: int = 4
    SERVICE_GALILEO: int = 8

    def __init__(
        self,
        *,
        status: int = ...,
        service: int = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def status(self) -> int: ...
    @status.setter
    def status(self, value: int) -> None: ...
    @property
    def service(self) -> int: ...
    @service.setter
    def service(self, value: int) -> None: ...
