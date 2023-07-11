# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import Field

from grafana_dashboard.utils import MyBaseModel


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


class BarAlignment(Enum):
    integer__1 = -1
    integer_0 = 0
    integer_1 = 1


class BarConfig(MyBaseModel):
    barAlignment: Optional[BarAlignment] = None
    barWidthFactor: Optional[float] = None
    barMaxWidth: Optional[float] = None


class FillConfig(MyBaseModel):
    fillColor: Optional[str] = None
    fillOpacity: Optional[float] = None
    fillBelowTo: Optional[str] = None


class GraphDrawStyle(Enum):
    line = 'line'
    bars = 'bars'
    points = 'points'


class GraphGradientMode(Enum):
    none = 'none'
    opacity = 'opacity'
    hue = 'hue'
    scheme = 'scheme'


class GraphTransform(Enum):
    constant = 'constant'
    negative_Y = 'negative-Y'


class GraphTresholdsStyleMode(Enum):
    off = 'off'
    line = 'line'
    dashed = 'dashed'
    area = 'area'
    line_area = 'line+area'
    dashed_area = 'dashed+area'
    series = 'series'


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


class LineInterpolation(Enum):
    linear = 'linear'
    smooth = 'smooth'
    stepBefore = 'stepBefore'
    stepAfter = 'stepAfter'


class Fill(Enum):
    solid = 'solid'
    dash = 'dash'
    dot = 'dot'
    square = 'square'


class LineStyle(MyBaseModel):
    fill: Optional[Fill] = None
    dash: Optional[List[float]] = None


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


class StackingMode(Enum):
    none = 'none'
    normal = 'normal'
    percent = 'percent'


class TimeZoneEnum(Enum):
    utc = 'utc'


class TimeZone(MyBaseModel):
    __root__: Optional[Union[TimeZoneEnum, Any]] = Field(
        'browser',
        description='A specific timezone from https://en.wikipedia.org/wiki/Tz_database',
    )


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
    showLegend: bool = True  # NOTE MODIFIED
    asTable: Optional[bool] = None
    isVisible: Optional[bool] = None
    sortBy: Optional[str] = None
    sortDesc: Optional[bool] = None
    width: Optional[float] = None
    calcs: List[str] = []  # NOTE MODIFIED


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


class GraphThresholdsStyleConfig(MyBaseModel):
    mode: GraphTresholdsStyleMode


class LineConfig(MyBaseModel):
    lineColor: Optional[str] = None
    lineWidth: Optional[float] = None
    lineInterpolation: Optional[LineInterpolation] = None
    lineStyle: Optional[LineStyle] = None
    spanNulls: Optional[Union[bool, float]] = Field(
        None,
        description='Indicate if null values should be treated as gaps or connected.\nWhen the value is a number, it represents the maximum delta in the\nX axis that should be considered connected.  For timeseries, this is milliseconds',
    )


class OptionsWithTimezones(MyBaseModel):
    timezone: Optional[List[TimeZone]] = None


class PointsConfig(MyBaseModel):
    showPoints: Optional[VisibilityMode] = None
    pointSize: Optional[float] = None
    pointColor: Optional[str] = None
    pointSymbol: Optional[str] = None


class StackingConfig(MyBaseModel):
    mode: Optional[StackingMode] = None
    group: Optional[str] = None


class PanelOptions(OptionsWithTimezones):
    legend: VizLegendOptions
    tooltip: VizTooltipOptions


class StackableFieldConfig(MyBaseModel):
    stacking: Optional[StackingConfig] = None


class GraphFieldConfig(
    LineConfig,
    FillConfig,
    PointsConfig,
    AxisConfig,
    BarConfig,
    StackableFieldConfig,
    HideableFieldConfig,
):
    drawStyle: Optional[GraphDrawStyle] = None
    gradientMode: Optional[GraphGradientMode] = None
    thresholdsStyle: Optional[GraphThresholdsStyleConfig] = None
    transform: Optional[GraphTransform] = None


class TimeSeriesPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
    PanelFieldConfig: GraphFieldConfig
