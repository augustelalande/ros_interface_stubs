# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class Point32:
    def __init__(
        self,
        *,
        x: float = ...,
        y: float = ...,
        z: float = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, value: float) -> None: ...
