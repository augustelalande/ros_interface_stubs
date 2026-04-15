# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import builtin_interfaces.msg

class QoSProfile:
    # Constants
    HISTORY_SYSTEM_DEFAULT: int = 0
    HISTORY_KEEP_LAST: int = 1
    HISTORY_KEEP_ALL: int = 2
    HISTORY_UNKNOWN: int = 3
    RELIABILITY_SYSTEM_DEFAULT: int = 0
    RELIABILITY_RELIABLE: int = 1
    RELIABILITY_BEST_EFFORT: int = 2
    RELIABILITY_UNKNOWN: int = 3
    RELIABILITY_BEST_AVAILABLE: int = 4
    DURABILITY_SYSTEM_DEFAULT: int = 0
    DURABILITY_TRANSIENT_LOCAL: int = 1
    DURABILITY_VOLATILE: int = 2
    DURABILITY_UNKNOWN: int = 3
    DURABILITY_BEST_AVAILABLE: int = 4
    LIVELINESS_SYSTEM_DEFAULT: int = 0
    LIVELINESS_AUTOMATIC: int = 1
    LIVELINESS_MANUAL_BY_TOPIC: int = 3
    LIVELINESS_UNKNOWN: int = 4
    LIVELINESS_BEST_AVAILABLE: int = 5

    def __init__(
        self,
        *,
        depth: int = ...,
        deadline: builtin_interfaces.msg.Duration = ...,
        lifespan: builtin_interfaces.msg.Duration = ...,
        history: int = ...,
        reliability: int = ...,
        durability: int = ...,
        liveliness: int = ...,
        liveliness_lease_duration: builtin_interfaces.msg.Duration = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def depth(self) -> int: ...
    @depth.setter
    def depth(self, value: int) -> None: ...
    @property
    def deadline(self) -> builtin_interfaces.msg.Duration: ...
    @deadline.setter
    def deadline(self, value: builtin_interfaces.msg.Duration) -> None: ...
    @property
    def lifespan(self) -> builtin_interfaces.msg.Duration: ...
    @lifespan.setter
    def lifespan(self, value: builtin_interfaces.msg.Duration) -> None: ...
    @property
    def history(self) -> int: ...
    @history.setter
    def history(self, value: int) -> None: ...
    @property
    def reliability(self) -> int: ...
    @reliability.setter
    def reliability(self, value: int) -> None: ...
    @property
    def durability(self) -> int: ...
    @durability.setter
    def durability(self, value: int) -> None: ...
    @property
    def liveliness(self) -> int: ...
    @liveliness.setter
    def liveliness(self, value: int) -> None: ...
    @property
    def liveliness_lease_duration(self) -> builtin_interfaces.msg.Duration: ...
    @liveliness_lease_duration.setter
    def liveliness_lease_duration(
        self, value: builtin_interfaces.msg.Duration
    ) -> None: ...
