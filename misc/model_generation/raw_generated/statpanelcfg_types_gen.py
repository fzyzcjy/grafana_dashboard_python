# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class BigValueColorMode(Enum):
    value = 'value'
    background = 'background'
    background_solid = 'background_solid'
    none = 'none'


class BigValueGraphMode(Enum):
    none = 'none'
    line = 'line'
    area = 'area'


class BigValueJustifyMode(Enum):
    auto = 'auto'
    center = 'center'


class BigValueTextMode(Enum):
    auto = 'auto'
    value = 'value'
    value_and_name = 'value_and_name'
    name = 'name'
    none = 'none'


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


class VizOrientation(Enum):
    auto = 'auto'
    vertical = 'vertical'
    horizontal = 'horizontal'


class VizTextDisplayOptions(BaseModel):
    titleSize: Optional[float] = Field(None, description='Explicit title text size')
    valueSize: Optional[float] = Field(None, description='Explicit value text size')


class OptionsWithTextFormatting(BaseModel):
    text: Optional[VizTextDisplayOptions] = None


class SingleStatBaseOptions(OptionsWithTextFormatting):
    reduceOptions: ReduceDataOptions
    orientation: VizOrientation


class PanelOptions(SingleStatBaseOptions):
    graphMode: BigValueGraphMode
    colorMode: BigValueColorMode
    justifyMode: BigValueJustifyMode
    textMode: BigValueTextMode


class StatPanelCfg(BaseModel):
    PanelOptions: PanelOptions
