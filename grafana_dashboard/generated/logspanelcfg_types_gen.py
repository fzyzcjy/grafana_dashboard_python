# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class LogsDedupStrategy(Enum):
    none = 'none'
    exact = 'exact'
    numbers = 'numbers'
    signature = 'signature'


class LogsSortOrder(Enum):
    Descending = 'Descending'
    Ascending = 'Ascending'


class PanelOptions(BaseModel):
    showLabels: bool
    showCommonLabels: bool
    showTime: bool
    wrapLogMessage: bool
    prettifyLogMessage: bool
    enableLogDetails: bool
    sortOrder: LogsSortOrder
    dedupStrategy: LogsDedupStrategy


class LogsPanelCfg(BaseModel):
    PanelOptions: PanelOptions
