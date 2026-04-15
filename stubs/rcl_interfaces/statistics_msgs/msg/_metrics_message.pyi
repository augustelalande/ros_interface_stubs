# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg
import statistics_msgs.msg

class MetricsMessage:
    def __init__(
        self,
        *,
        measurement_source_name: str = ...,
        metrics_source: str = ...,
        unit: str = ...,
        window_start: builtin_interfaces.msg.Time = ...,
        window_stop: builtin_interfaces.msg.Time = ...,
        statistics: list[statistics_msgs.msg.StatisticDataPoint] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def measurement_source_name(self) -> str: ...
    @measurement_source_name.setter
    def measurement_source_name(self, value: str) -> None: ...
    @property
    def metrics_source(self) -> str: ...
    @metrics_source.setter
    def metrics_source(self, value: str) -> None: ...
    @property
    def unit(self) -> str: ...
    @unit.setter
    def unit(self, value: str) -> None: ...
    @property
    def window_start(self) -> builtin_interfaces.msg.Time: ...
    @window_start.setter
    def window_start(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def window_stop(self) -> builtin_interfaces.msg.Time: ...
    @window_stop.setter
    def window_stop(self, value: builtin_interfaces.msg.Time) -> None: ...
    @property
    def statistics(self) -> list[statistics_msgs.msg.StatisticDataPoint]: ...
    @statistics.setter
    def statistics(
        self, value: list[statistics_msgs.msg.StatisticDataPoint]
    ) -> None: ...
