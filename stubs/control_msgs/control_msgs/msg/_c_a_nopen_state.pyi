# This file was generated automatically by
# `scripts/generate_stubs.py`.
# Do not modify it manually. If needed re-run the script.

class CANopenState:
    # Constants
    NMT_INITIALISING: int = 0
    NMT_PRE_OPERATIONAL: int = 127
    NMT_OPERATIONAL: int = 5
    NMT_STOPPED: int = 4
    DSP402_NOT_READY_TO_SWITCH_ON: int = 0
    DSP402_SWITCH_ON_DISABLED: int = 1
    DSP402_READY_TO_SWITCH_ON: int = 2
    DSP402_SWITCHED_ON: int = 3
    DSP402_OPERATION_ENABLED: int = 4
    DSP402_QUICK_STOP_ACTIVE: int = 5
    DSP402_FAULT_REACTION_ACTIVE: int = 6
    DSP402_FAULT: int = 7

    def __init__(
        self,
        *,
        node_id: int = ...,
        nmt_state: int = ...,
        dsp_402_state: int = ...,
        last_emcy_code: int = ...,
    ) -> None: ...
    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]: ...

    # Members
    @property
    def node_id(self) -> int: ...
    @node_id.setter
    def node_id(self, value: int) -> None: ...
    @property
    def nmt_state(self) -> int: ...
    @nmt_state.setter
    def nmt_state(self, value: int) -> None: ...
    @property
    def dsp_402_state(self) -> int: ...
    @dsp_402_state.setter
    def dsp_402_state(self, value: int) -> None: ...
    @property
    def last_emcy_code(self) -> int: ...
    @last_emcy_code.setter
    def last_emcy_code(self, value: int) -> None: ...
