# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from __future__ import annotations

from pydantic import Field, confloat, conint

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


class GraphGradientMode(Enum):
    none = 'none'
    opacity = 'opacity'
    hue = 'hue'
    scheme = 'scheme'


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


class ScaleDistribution(Enum):
    linear = 'linear'
    log = 'log'
    ordinal = 'ordinal'
    symlog = 'symlog'


class ScaleDistributionConfig(MyBaseModel):
    type: ScaleDistribution
    log: Optional[float] = None
    linearThreshold: Optional[float] = None


class StackingMode(Enum):
    none = 'none'
    normal = 'normal'
    percent = 'percent'


class VisibilityMode(Enum):
    auto = 'auto'
    never = 'never'
    always = 'always'


class VizOrientation(Enum):
    auto = 'auto'
    vertical = 'vertical'
    horizontal = 'horizontal'


class VizTextDisplayOptions(MyBaseModel):
    titleSize: Optional[float] = Field(None, description='Explicit title text size')
    valueSize: Optional[float] = Field(None, description='Explicit value text size')


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


class OptionsWithLegend(MyBaseModel):
    legend: VizLegendOptions


class OptionsWithTextFormatting(MyBaseModel):
    text: Optional[VizTextDisplayOptions] = None


class OptionsWithTooltip(MyBaseModel):
    tooltip: VizTooltipOptions


class PanelOptions(OptionsWithLegend, OptionsWithTooltip, OptionsWithTextFormatting):
    xField: Optional[str] = Field(
        None,
        description='Manually select which field from the dataset to represent the x field.',
    )
    colorByField: Optional[str] = Field(
        None,
        description='Use the color value for a sibling field to color each bar value.',
    )
    orientation: VizOrientation = Field(
        ...,
        description='Controls the orientation of the bar chart, either vertical or horizontal.',
    )
    barRadius: Optional[confloat(ge=0.0, le=0.5)] = Field(
        0, description='Controls the radius of each bar.'
    )
    xTickLabelRotation: conint(ge=-90, le=90) = Field(
        ..., description='Controls the rotation of the x axis labels.'
    )
    xTickLabelMaxLength: conint(ge=0, le=2147483647) = Field(
        ...,
        description='Sets the max length that a label can have before it is truncated.',
    )
    xTickLabelSpacing: Optional[conint(ge=-2147483648, le=2147483647)] = Field(
        0,
        description='Controls the spacing between x axis labels.\nnegative values indicate backwards skipping behavior',
    )
    stacking: StackingMode = Field(
        ...,
        description='Controls whether bars are stacked or not, either normally or in percent mode.',
    )
    showValue: VisibilityMode = Field(
        ...,
        description='This controls whether values are shown on top or to the left of bars.',
    )
    barWidth: confloat(ge=0.0, le=1.0) = Field(
        ..., description='Controls the width of bars. 1 = Max width, 0 = Min width.'
    )
    groupWidth: confloat(ge=0.0, le=1.0) = Field(
        ..., description='Controls the width of groups. 1 = max with, 0 = min width.'
    )
    fullHighlight: bool = Field(
        ...,
        description='Enables mode which highlights the entire bar area and shows tooltip when cursor\nhovers over highlighted area',
    )


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
    thresholdsStyle: Optional[GraphThresholdsStyleConfig] = None


class BarChartPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
    PanelFieldConfig: PanelFieldConfig
