# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from __future__ import annotations

from typing import Any, Union

from pydantic import Field, confloat, conint

from grafana_dashboard.extracted_generated_common_models import *
from grafana_dashboard.utils import MyBaseModel


class HideSeriesConfig(MyBaseModel):
    tooltip: bool
    legend: bool
    viz: bool


class HideableFieldConfig(MyBaseModel):
    hideFrom: Optional[HideSeriesConfig] = None


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


class VisibilityMode(Enum):
    auto = 'auto'
    never = 'never'
    always = 'always'


class OptionsWithLegend(MyBaseModel):
    legend: VizLegendOptions = VizLegendOptions()  # NOTE MODIFIED


class OptionsWithTimezones(MyBaseModel):
    timezone: Optional[List[TimeZone]] = None


class OptionsWithTooltip(MyBaseModel):
    tooltip: VizTooltipOptions = VizTooltipOptions()  # NOTE MODIFIED


class PanelOptions(OptionsWithLegend, OptionsWithTooltip, OptionsWithTimezones):
    showValue: VisibilityMode = Field(VisibilityMode.auto, description='Show timeline values on chart')  # NOTE MODIFIED
    rowHeight: confloat(le=1.0) = Field(0.9, description='Controls the row height')  # NOTE MODIFIED
    mergeValues: Optional[bool] = Field(
        True, description='Merge equal consecutive values'
    )
    alignValue: Optional[TimelineValueAlignment] = Field(
        TimelineValueAlignment.left, description='Controls value alignment on the timelines'  # NOTE MODIFIED
    )


class StateTimelinePanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
    PanelFieldConfig: PanelFieldConfig
