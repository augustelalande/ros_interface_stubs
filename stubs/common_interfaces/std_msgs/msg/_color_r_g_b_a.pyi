# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class ColorRGBA:
    def __init__(
        self,
        *,
        r: float = ...,
        g: float = ...,
        b: float = ...,
        a: float = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def r(self) -> float: ...
    @r.setter
    def r(self, value: float) -> None: ...
    @property
    def g(self) -> float: ...
    @g.setter
    def g(self, value: float) -> None: ...
    @property
    def b(self) -> float: ...
    @b.setter
    def b(self, value: float) -> None: ...
    @property
    def a(self) -> float: ...
    @a.setter
    def a(self, value: float) -> None: ...
