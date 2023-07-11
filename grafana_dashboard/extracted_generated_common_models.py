from enum import Enum
from typing import Optional, List

from grafana_dashboard.utils import MyBaseModel


# NOTE this is currently *manually* extracted (but may be automated later)

class LegendDisplayMode(Enum):
    list = 'list'
    table = 'table'
    hidden = 'hidden'


class LegendPlacement(Enum):
    bottom = 'bottom'
    right = 'right'


class VizLegendOptions(MyBaseModel):
    displayMode: LegendDisplayMode = LegendDisplayMode.list  # NOTE MODIFIED
    placement: LegendPlacement = LegendPlacement.bottom  # NOTE MODIFIED
    showLegend: bool = True  # NOTE MODIFIED
    asTable: Optional[bool] = None
    isVisible: Optional[bool] = None
    sortBy: Optional[str] = None
    sortDesc: Optional[bool] = None
    width: Optional[float] = None
    calcs: List[str] = []  # NOTE MODIFIED


class TooltipDisplayMode(Enum):
    single = 'single'
    multi = 'multi'
    none = 'none'


class SortOrder(Enum):
    asc = 'asc'
    desc = 'desc'
    none = 'none'


class VizTooltipOptions(MyBaseModel):
    mode: TooltipDisplayMode = TooltipDisplayMode.single  # NOTE MODIFIED
    sort: SortOrder = SortOrder.none  # NOTE MODIFIED
