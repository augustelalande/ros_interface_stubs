# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class MenuEntry:
    # Constants
    FEEDBACK: int = 0
    ROSRUN: int = 1
    ROSLAUNCH: int = 2

    def __init__(
        self,
        *,
        id: int = ...,  # noqa: A002
        parent_id: int = ...,
        title: str = ...,
        command: str = ...,
        command_type: int = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, value: int) -> None: ...
    @property
    def parent_id(self) -> int: ...
    @parent_id.setter
    def parent_id(self, value: int) -> None: ...
    @property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    @property
    def command(self) -> str: ...
    @command.setter
    def command(self, value: str) -> None: ...
    @property
    def command_type(self) -> int: ...
    @command_type.setter
    def command_type(self, value: int) -> None: ...
