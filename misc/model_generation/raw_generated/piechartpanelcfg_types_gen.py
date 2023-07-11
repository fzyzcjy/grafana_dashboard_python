# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class HideSeriesConfig(BaseModel):
    tooltip: bool
    legend: bool
    viz: bool


class HideableFieldConfig(BaseModel):
    hideFrom: Optional[HideSeriesConfig] = None


class LegendDisplayMode(Enum):
    list = 'list'
    table = 'table'
    hidden = 'hidden'


class LegendPlacement(Enum):
    bottom = 'bottom'
    right = 'right'


class PieChartLabels(Enum):
    name = 'name'
    value = 'value'
    percent = 'percent'


class PieChartLegendValues(Enum):
    value = 'value'
    percent = 'percent'


class PieChartType(Enum):
    pie = 'pie'
    donut = 'donut'


class ReduceDataOptions(BaseModel):
    values: Optional[bool] = Field(None, description='If true show each row value')
    limit: Optional[float] = Field(None, description='if showing all values limit')
    calcs: List[str] = Field(
        ..., description='When !values, pick one value for the whole field'
    )
    fields: Optional[str] = Field(
        None,
        description='Which fields to show.  By default this is only numeric fields',
    )


class SortOrder(Enum):
    asc = 'asc'
    desc = 'desc'
    none = 'none'


class TooltipDisplayMode(Enum):
    single = 'single'
    multi = 'multi'
    none = 'none'


class VizLegendOptions(BaseModel):
    displayMode: LegendDisplayMode
    placement: LegendPlacement
    showLegend: bool
    asTable: Optional[bool] = None
    isVisible: Optional[bool] = None
    sortBy: Optional[str] = None
    sortDesc: Optional[bool] = None
    width: Optional[float] = None
    calcs: List[str]


class VizOrientation(Enum):
    auto = 'auto'
    vertical = 'vertical'
    horizontal = 'horizontal'


class VizTextDisplayOptions(BaseModel):
    titleSize: Optional[float] = Field(None, description='Explicit title text size')
    valueSize: Optional[float] = Field(None, description='Explicit value text size')


class VizTooltipOptions(BaseModel):
    mode: TooltipDisplayMode
    sort: SortOrder


class OptionsWithTextFormatting(BaseModel):
    text: Optional[VizTextDisplayOptions] = None


class OptionsWithTooltip(BaseModel):
    tooltip: VizTooltipOptions


class PieChartLegendOptions(VizLegendOptions):
    values: List[PieChartLegendValues]


class SingleStatBaseOptions(OptionsWithTextFormatting):
    reduceOptions: ReduceDataOptions
    orientation: VizOrientation


class PanelOptions(OptionsWithTooltip, SingleStatBaseOptions):
    pieType: PieChartType
    displayLabels: List[PieChartLabels]
    legend: PieChartLegendOptions


class PieChartPanelCfg(BaseModel):
    PieChartType: PieChartType = Field(
        ..., description='Select the pie chart display style.'
    )
    PieChartLabels: PieChartLabels = Field(
        ...,
        description='Select labels to display on the pie chart.\n - Name - The series or field name.\n - Percent - The percentage of the whole.\n - Value - The raw numerical value.',
    )
    PieChartLegendValues: PieChartLegendValues = Field(
        ...,
        description='Select values to display in the legend.\n - Percent: The percentage of the whole.\n - Value: The raw numerical value.',
    )
    PieChartLegendOptions: PieChartLegendOptions
    PanelOptions: PanelOptions
    PanelFieldConfig: HideableFieldConfig
