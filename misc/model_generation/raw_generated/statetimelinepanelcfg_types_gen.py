# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field, confloat, conint


class HideSeriesConfig(MyBaseModel):
    tooltip: bool
    legend: bool
    viz: bool


class HideableFieldConfig(MyBaseModel):
    hideFrom: Optional[HideSeriesConfig] = None


class LegendDisplayMode(Enum):
    list = 'list'
    table = 'table'
    hidden = 'hidden'


class LegendPlacement(Enum):
    bottom = 'bottom'
    right = 'right'


class SortOrder(Enum):
    asc = 'asc'
    desc = 'desc'
    none = 'none'


class PanelFieldConfig(HideableFieldConfig):
    lineWidth: Optional[conint(ge=0, le=10)] = 0
    fillOpacity: Optional[conint(ge=0, le=100)] = 70


class TimeZoneEnum(Enum):
    utc = 'utc'


class TimeZone(MyBaseModel):
    __root__: Optional[Union[TimeZoneEnum, Any]] = Field(
        'browser',
        description='A specific timezone from https://en.wikipedia.org/wiki/Tz_database',
    )


class TimelineValueAlignment(Enum):
    center = 'center'
    left = 'left'
    right = 'right'


class TooltipDisplayMode(Enum):
    single = 'single'
    multi = 'multi'
    none = 'none'


class VisibilityMode(Enum):
    auto = 'auto'
    never = 'never'
    always = 'always'


class VizLegendOptions(MyBaseModel):
    displayMode: LegendDisplayMode
    placement: LegendPlacement
    showLegend: bool
    asTable: Optional[bool] = None
    isVisible: Optional[bool] = None
    sortBy: Optional[str] = None
    sortDesc: Optional[bool] = None
    width: Optional[float] = None
    calcs: List[str]


class VizTooltipOptions(MyBaseModel):
    mode: TooltipDisplayMode
    sort: SortOrder


class OptionsWithLegend(MyBaseModel):
    legend: VizLegendOptions


class OptionsWithTimezones(MyBaseModel):
    timezone: Optional[List[TimeZone]] = None


class OptionsWithTooltip(MyBaseModel):
    tooltip: VizTooltipOptions


class PanelOptions(OptionsWithLegend, OptionsWithTooltip, OptionsWithTimezones):
    showValue: VisibilityMode = Field(..., description='Show timeline values on chart')
    rowHeight: confloat(le=1.0) = Field(..., description='Controls the row height')
    mergeValues: Optional[bool] = Field(
        True, description='Merge equal consecutive values'
    )
    alignValue: Optional[TimelineValueAlignment] = Field(
        None, description='Controls value alignment on the timelines'
    )


class StateTimelinePanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
    PanelFieldConfig: PanelFieldConfig
