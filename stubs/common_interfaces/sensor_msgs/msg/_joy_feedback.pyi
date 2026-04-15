# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class JoyFeedback:
    # Constants
    TYPE_LED: int = 0
    TYPE_RUMBLE: int = 1
    TYPE_BUZZER: int = 2

    def __init__(
        self,
        *,
        type: int = ...,  # noqa: A002
        id: int = ...,  # noqa: A002
        intensity: float = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def type(self) -> int: ...
    @type.setter
    def type(self, value: int) -> None: ...
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, value: int) -> None: ...
    @property
    def intensity(self) -> float: ...
    @intensity.setter
    def intensity(self, value: float) -> None: ...
