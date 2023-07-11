# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field, conint


class AxisColorMode(Enum):
    text = 'text'
    series = 'series'


class AxisPlacement(Enum):
    auto = 'auto'
    top = 'top'
    right = 'right'
    bottom = 'bottom'
    left = 'left'
    hidden = 'hidden'


class GraphGradientMode(Enum):
    none = 'none'
    opacity = 'opacity'
    hue = 'hue'
    scheme = 'scheme'


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


class ScaleDistribution(Enum):
    linear = 'linear'
    log = 'log'
    ordinal = 'ordinal'
    symlog = 'symlog'


class ScaleDistributionConfig(MyBaseModel):
    type: ScaleDistribution
    log: Optional[float] = None
    linearThreshold: Optional[float] = None


class SortOrder(Enum):
    asc = 'asc'
    desc = 'desc'
    none = 'none'


class TooltipDisplayMode(Enum):
    single = 'single'
    multi = 'multi'
    none = 'none'


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


class AxisConfig(MyBaseModel):
    axisPlacement: Optional[AxisPlacement] = None
    axisColorMode: Optional[AxisColorMode] = None
    axisLabel: Optional[str] = None
    axisWidth: Optional[float] = None
    axisSoftMin: Optional[float] = None
    axisSoftMax: Optional[float] = None
    axisGridShow: Optional[bool] = None
    scaleDistribution: Optional[ScaleDistributionConfig] = None
    axisCenteredZero: Optional[bool] = None


class PanelFieldConfig(AxisConfig, HideableFieldConfig):
    lineWidth: Optional[conint(ge=0, le=10)] = Field(
        1, description='Controls line width of the bars.'
    )
    fillOpacity: Optional[conint(ge=0, le=100)] = Field(
        80, description='Controls the fill opacity of the bars.'
    )
    gradientMode: Optional[GraphGradientMode] = Field(
        None,
        description='Set the mode of the gradient fill. Fill gradient is based on the line color. To change the color, use the standard color scheme field option.\nGradient appearance is influenced by the Fill opacity setting.',
    )


class OptionsWithLegend(MyBaseModel):
    legend: VizLegendOptions


class OptionsWithTooltip(MyBaseModel):
    tooltip: VizTooltipOptions


class PanelOptions(OptionsWithLegend, OptionsWithTooltip):
    bucketSize: Optional[int] = Field(None, description='Size of each bucket')
    bucketOffset: Optional[conint(ge=-2147483648, le=2147483647)] = Field(
        0, description='Offset buckets by this amount'
    )
    combine: Optional[bool] = Field(
        None, description='Combines multiple series into a single histogram'
    )


class HistogramPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
    PanelFieldConfig: PanelFieldConfig
