# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND


from enum import Enum
from typing import Any, Optional, Union

from pydantic import Field, conint

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


class CellValues(MyBaseModel):
    unit: Optional[str] = Field(None, description='Controls the cell value unit')
    decimals: Optional[float] = Field(
        None, description='Controls the number of decimals for cell values'
    )


class ExemplarConfig(MyBaseModel):
    color: str = Field(..., description='Sets the color of the exemplar markers')


class FilterValueRange(MyBaseModel):
    le: Optional[float] = Field(
        None,
        description='Sets the filter range to values less than or equal to the given value',
    )
    ge: Optional[float] = Field(
        None,
        description='Sets the filter range to values greater than or equal to the given value',
    )


class HeatmapCalculationMode(Enum):
    size = 'size'
    count = 'count'


class HeatmapCellLayout(Enum):
    le = 'le'
    ge = 'ge'
    unknown = 'unknown'
    auto = 'auto'


class HeatmapColorMode(Enum):
    opacity = 'opacity'
    scheme = 'scheme'


class HeatmapColorScale(Enum):
    linear = 'linear'
    exponential = 'exponential'


class HeatmapLegend(MyBaseModel):
    show: bool = Field(..., description='Controls if the legend is shown')


class HeatmapColorOptions(MyBaseModel):
    mode: Optional[HeatmapColorMode] = None
    scheme: str = Field(..., description='Controls the color scheme used')
    fill: str = Field(..., description='Controls the color fill when in opacity mode')
    scale: Optional[HeatmapColorScale] = None
    exponent: float = Field(
        ..., description='Controls the exponent when scale is set to exponential'
    )
    steps: conint(ge=2, le=128) = Field(
        ..., description='Controls the number of color steps'
    )
    reverse: bool = Field(..., description='Reverses the color scheme')
    min: Optional[float] = Field(
        None, description='Sets the minimum value for the color scale'
    )
    max: Optional[float] = Field(
        None, description='Sets the maximum value for the color scale'
    )


class HeatmapTooltip(MyBaseModel):
    show: bool = Field(..., description='Controls if the tooltip is shown')
    yHistogram: Optional[bool] = Field(
        None,
        description='Controls if the tooltip shows a histogram of the y-axis values',
    )


class RowsHeatmapOptions(MyBaseModel):
    value: Optional[str] = Field(
        None, description='Sets the name of the cell when not calculating from data'
    )
    layout: Optional[HeatmapCellLayout] = None


class Scheme(Enum):
    Oranges = 'Oranges'


class Fill(Enum):
    dark_orange = 'dark-orange'


class Reverse(Enum):
    boolean_False = False


class Exponent(Enum):
    number_0_5 = 0.5


class Steps(Enum):
    integer_64 = 64


class ColorItem(MyBaseModel):
    scheme: Scheme = Field(
        ...,
        description='mode:     HeatmapColorMode // TODO: fix after remove when https://github.com/grafana/cuetsy/issues/74 is fixed',
    )
    fill: Fill
    reverse: Reverse = Field(
        ...,
        description='scale:    HeatmapColorScale // TODO: fix after remove when https://github.com/grafana/cuetsy/issues/74 is fixed',
    )
    exponent: Exponent
    steps: Steps


class Le(Enum):
    field_1e_09 = '1e-09'


class FilterValue(MyBaseModel):
    le: Le


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


class VisibilityMode(Enum):
    auto = 'auto'
    never = 'never'
    always = 'always'


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


class HeatmapCalculationBucketConfig(MyBaseModel):
    mode: Optional[HeatmapCalculationMode] = None
    value: Optional[str] = Field(
        None, description='The number of buckets to use for the axis in the heatmap'
    )
    scale: Optional[ScaleDistributionConfig] = None


class HeatmapCalculationOptions(MyBaseModel):
    xBuckets: Optional[HeatmapCalculationBucketConfig] = None
    yBuckets: Optional[HeatmapCalculationBucketConfig] = None


class YAxisConfig(AxisConfig):
    unit: Optional[str] = Field(None, description='Sets the yAxis unit')
    reverse: Optional[bool] = Field(None, description='Reverses the yAxis')
    decimals: Optional[float] = Field(
        None, description='Controls the number of decimals for yAxis values'
    )
    min: Optional[float] = Field(
        None, description='Sets the minimum value for the yAxis'
    )
    max: Optional[float] = Field(
        None, description='Sets the maximum value for the yAxis'
    )


class PanelFieldConfig(HideableFieldConfig):
    scaleDistribution: Optional[ScaleDistributionConfig] = None


class PanelOptions(MyBaseModel):
    calculate: Optional[bool] = Field(
        False, description='Controls if the heatmap should be calculated from data'
    )
    calculation: Optional[HeatmapCalculationOptions] = None
    color: Optional[Union[HeatmapColorOptions, ColorItem]] = Field(
        {
            'scheme': 'Oranges',
            'fill': 'dark-orange',
            'reverse': False,
            'exponent': 0.5,
            'steps': 64,
        },
        description='Controls the color options',
    )
    filterValues: Optional[Union[FilterValueRange, FilterValue]] = Field(
        {'le': '1e-09'}, description='Filters values between a given range'
    )
    rowsFrame: Optional[RowsHeatmapOptions] = None
    showValue: VisibilityMode = Field(
        ...,
        description='| *{\n\tlayout: ui.HeatmapCellLayout & "auto" // TODO: fix after remove when https://github.com/grafana/cuetsy/issues/74 is fixed\n}\nControls the display of the value in the cell',
    )
    cellGap: Optional[conint(ge=0, le=25)] = Field(
        1, description='Controls gap between cells'
    )
    cellRadius: Optional[float] = Field(None, description='Controls cell radius')
    cellValues: Optional[Union[CellValues, Any]] = Field(
        {}, description='Controls cell value unit'
    )
    yAxis: YAxisConfig
    legend: HeatmapLegend
    tooltip: HeatmapTooltip
    exemplars: ExemplarConfig


class HeatmapPanelCfg(MyBaseModel):
    HeatmapColorMode: HeatmapColorMode = Field(
        ..., description='Controls the color mode of the heatmap'
    )
    HeatmapColorScale: HeatmapColorScale = Field(
        ..., description='Controls the color scale of the heatmap'
    )
    HeatmapColorOptions: HeatmapColorOptions = Field(
        ..., description='Controls various color options'
    )
    YAxisConfig: YAxisConfig = Field(
        ..., description='Configuration options for the yAxis'
    )
    CellValues: CellValues = Field(..., description='Controls cell value options')
    FilterValueRange: FilterValueRange = Field(
        ..., description='Controls the value filter range'
    )
    HeatmapTooltip: HeatmapTooltip = Field(..., description='Controls tooltip options')
    HeatmapLegend: HeatmapLegend = Field(..., description='Controls legend options')
    ExemplarConfig: ExemplarConfig = Field(..., description='Controls exemplar options')
    RowsHeatmapOptions: RowsHeatmapOptions = Field(
        ..., description='Controls frame rows options'
    )
    PanelOptions: PanelOptions
    PanelFieldConfig: PanelFieldConfig
