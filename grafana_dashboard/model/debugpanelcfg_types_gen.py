# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND


from enum import Enum
from typing import Optional

from grafana_dashboard.utils import MyBaseModel


class DebugMode(Enum):
    render = 'render'
    events = 'events'
    cursor = 'cursor'
    State = 'State'
    ThrowError = 'ThrowError'


class UpdateConfig(MyBaseModel):
    render: bool
    dataChanged: bool
    schemaChanged: bool


class PanelOptions(MyBaseModel):
    mode: DebugMode
    counters: Optional[UpdateConfig] = None


class DebugPanelCfg(MyBaseModel):
    UpdateConfig: UpdateConfig
    DebugMode: DebugMode
    PanelOptions: PanelOptions
