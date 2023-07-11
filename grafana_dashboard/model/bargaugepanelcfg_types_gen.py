# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field, conint


class BarGaugeDisplayMode(Enum):
    basic = 'basic'
    lcd = 'lcd'
    gradient = 'gradient'


class BarGaugeValueMode(Enum):
    color = 'color'
    text = 'text'
    hidden = 'hidden'


class ReduceDataOptions(MyBaseModel):
    values: Optional[bool] = Field(None, description='If true show each row value')
    limit: Optional[float] = Field(None, description='if showing all values limit')
    calcs: List[str] = Field(
        ..., description='When !values, pick one value for the whole field'
    )
    fields: Optional[str] = Field(
        None,
        description='Which fields to show.  By default this is only numeric fields',
    )


class VizOrientation(Enum):
    auto = 'auto'
    vertical = 'vertical'
    horizontal = 'horizontal'


class VizTextDisplayOptions(MyBaseModel):
    titleSize: Optional[float] = Field(None, description='Explicit title text size')
    valueSize: Optional[float] = Field(None, description='Explicit value text size')


class OptionsWithTextFormatting(MyBaseModel):
    text: Optional[VizTextDisplayOptions] = None


class SingleStatBaseOptions(OptionsWithTextFormatting):
    reduceOptions: ReduceDataOptions
    orientation: VizOrientation


class PanelOptions(SingleStatBaseOptions):
    displayMode: BarGaugeDisplayMode
    valueMode: BarGaugeValueMode
    showUnfilled: bool
    minVizWidth: conint(ge=0, le=4294967295)
    minVizHeight: conint(ge=0, le=4294967295)


class BarGaugePanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
