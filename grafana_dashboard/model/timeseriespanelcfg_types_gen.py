# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from typing import Any, Union

from pydantic import Field

from grafana_dashboard.extracted_generated_common_models import *
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
    barAlignment: Optional[BarAlignment] = BarAlignment.integer_0  # NOTE MODIFIED
    barWidthFactor: Optional[float] = None
    barMaxWidth: Optional[float] = None


class FillConfig(MyBaseModel):
    fillColor: Optional[str] = None
    fillOpacity: Optional[float] = 0  # NOTE MODIFIED
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
    tooltip: bool = False  # NOTE MODIFIED
    legend: bool = False  # NOTE MODIFIED
    viz: bool = False  # NOTE MODIFIED


class HideableFieldConfig(MyBaseModel):
    hideFrom: Optional[HideSeriesConfig] = HideSeriesConfig()  # NOTE MODIFIED


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
    type: ScaleDistribution = ScaleDistribution.linear  # NOTE MODIFIED
    log: Optional[float] = 2  # NOTE MODIFIED
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


class VizTooltipOptions(MyBaseModel):
    mode: TooltipDisplayMode = TooltipDisplayMode.single  # NOTE MODIFIED
    sort: SortOrder = SortOrder.none  # NOTE MODIFIED


class AxisConfig(MyBaseModel):
    axisPlacement: Optional[AxisPlacement] = AxisPlacement.auto  # NOTE MODIFIED
    axisColorMode: Optional[AxisColorMode] = None
    axisLabel: Optional[str] = ''  # NOTE MODIFIED
    axisWidth: Optional[float] = None
    axisSoftMin: Optional[float] = None
    axisSoftMax: Optional[float] = None
    axisGridShow: Optional[bool] = None
    scaleDistribution: Optional[ScaleDistributionConfig] = ScaleDistributionConfig()  # NOTE MODIFIED
    axisCenteredZero: Optional[bool] = None


class GraphThresholdsStyleConfig(MyBaseModel):
    mode: GraphTresholdsStyleMode = GraphTresholdsStyleMode.off  # NOTE MODIFIED


class LineConfig(MyBaseModel):
    lineColor: Optional[str] = None
    lineWidth: Optional[float] = 1  # NOTE MODIFIED
    lineInterpolation: Optional[LineInterpolation] = LineInterpolation.linear  # NOTE MODIFIED
    lineStyle: Optional[LineStyle] = None
    spanNulls: Optional[Union[bool, float]] = Field(
        False,  # NOTE MODIFIED
        description='Indicate if null values should be treated as gaps or connected.\nWhen the value is a number, it represents the maximum delta in the\nX axis that should be considered connected.  For timeseries, this is milliseconds',
    )


class OptionsWithTimezones(MyBaseModel):
    timezone: Optional[List[TimeZone]] = None


class PointsConfig(MyBaseModel):
    showPoints: Optional[VisibilityMode] = VisibilityMode.auto  # NOTE MODIFIED
    pointSize: Optional[float] = 5  # NOTE MODIFIED
    pointColor: Optional[str] = None
    pointSymbol: Optional[str] = None


class StackingConfig(MyBaseModel):
    mode: Optional[StackingMode] = None
    group: Optional[str] = None


class PanelOptions(OptionsWithTimezones):
    legend: VizLegendOptions = VizLegendOptions()  # NOTE MODIFIED
    tooltip: VizTooltipOptions = VizTooltipOptions()  # NOTE MODIFIED


class StackableFieldConfig(MyBaseModel):
    stacking: Optional[StackingConfig] = StackingConfig()  # NOTE MODIFIED


class GraphFieldConfig(
    LineConfig,
    FillConfig,
    PointsConfig,
    AxisConfig,
    BarConfig,
    StackableFieldConfig,
    HideableFieldConfig,
):
    drawStyle: Optional[GraphDrawStyle] = GraphDrawStyle.line  # NOTE MODIFIED
    gradientMode: Optional[GraphGradientMode] = GraphGradientMode.none  # NOTE MODIFIED
    thresholdsStyle: Optional[GraphThresholdsStyleConfig] = GraphThresholdsStyleConfig()  # NOTE MODIFIED
    transform: Optional[GraphTransform] = None


class TimeSeriesPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
    PanelFieldConfig: GraphFieldConfig
