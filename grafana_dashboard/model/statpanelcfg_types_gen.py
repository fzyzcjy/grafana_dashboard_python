# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import Field

from grafana_dashboard.utils import MyBaseModel


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


class ReduceDataOptions(MyBaseModel):
    values: Optional[bool] = Field(False, description='If true show each row value')  # NOTE MODIFIED
    limit: Optional[float] = Field(None, description='if showing all values limit')
    calcs: List[str] = Field(
        [], description='When !values, pick one value for the whole field'  # NOTE MODIFIED
    )
    fields: Optional[str] = Field(
        '',  # NOTE MODIFIED
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
    reduceOptions: ReduceDataOptions = ReduceDataOptions()  # NOTE MODIFIED
    orientation: VizOrientation = VizOrientation.auto  # NOTE MODIFIED


class PanelOptions(SingleStatBaseOptions):
    graphMode: BigValueGraphMode = BigValueGraphMode.area  # NOTE MODIFIED
    colorMode: BigValueColorMode = BigValueColorMode.value  # NOTE MODIFIED
    justifyMode: BigValueJustifyMode = BigValueJustifyMode.auto  # NOTE MODIFIED
    textMode: BigValueTextMode = BigValueTextMode.auto  # NOTE MODIFIED


class StatPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
