# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from grafana_dashboard.extracted_generated_common_models import *

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
    showLabels: bool
    showCommonLabels: bool
    showTime: bool
    wrapLogMessage: bool
    prettifyLogMessage: bool
    enableLogDetails: bool
    sortOrder: LogsSortOrder
    dedupStrategy: LogsDedupStrategy


class LogsPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
