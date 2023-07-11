# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum

from grafana_dashboard.utils import MyBaseModel


class LogsDedupStrategy(Enum):
    none = 'none'
    exact = 'exact'
    numbers = 'numbers'
    signature = 'signature'


class LogsSortOrder(Enum):
    Descending = 'Descending'
    Ascending = 'Ascending'


class PanelOptions(MyBaseModel):
    showLabels: bool = False  # NOTE MODIFIED
    showCommonLabels: bool = False  # NOTE MODIFIED
    showTime: bool = False  # NOTE MODIFIED
    wrapLogMessage: bool = False  # NOTE MODIFIED # NOTE MODIFIED
    prettifyLogMessage: bool = False  # NOTE MODIFIED
    enableLogDetails: bool = False  # NOTE MODIFIED
    sortOrder: LogsSortOrder = LogsSortOrder.Descending  # NOTE MODIFIED
    dedupStrategy: LogsDedupStrategy = LogsDedupStrategy.none  # NOTE MODIFIED


class LogsPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
