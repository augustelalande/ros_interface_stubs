# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class StatisticDataPoint:
    def __init__(
        self,
        *,
        data_type: int = ...,
        data: float = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def data_type(self) -> int: ...
    @data_type.setter
    def data_type(self, value: int) -> None: ...
    @property
    def data(self) -> float: ...
    @data.setter
    def data(self, value: float) -> None: ...
