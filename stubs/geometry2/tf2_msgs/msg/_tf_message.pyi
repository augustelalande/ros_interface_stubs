# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

import geometry_msgs.msg

class TFMessage:
    def __init__(
        self,
        *,
        transforms: list[geometry_msgs.msg.TransformStamped] = ...,
        check_fields: bool = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def transforms(self) -> list[geometry_msgs.msg.TransformStamped]: ...
    @transforms.setter
    def transforms(self, value: list[geometry_msgs.msg.TransformStamped]) -> None: ...
