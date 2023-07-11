# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class DebugMode(Enum):
    render = 'render'
    events = 'events'
    cursor = 'cursor'
    State = 'State'
    ThrowError = 'ThrowError'


class UpdateConfig(BaseModel):
    render: bool
    dataChanged: bool
    schemaChanged: bool


class PanelOptions(BaseModel):
    mode: DebugMode
    counters: Optional[UpdateConfig] = None


class DebugPanelCfg(BaseModel):
    UpdateConfig: UpdateConfig
    DebugMode: DebugMode
    PanelOptions: PanelOptions
