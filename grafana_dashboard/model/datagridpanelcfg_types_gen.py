# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND


from typing import Optional

from pydantic import conint

from grafana_dashboard.utils import MyBaseModel


class PanelOptions(MyBaseModel):
    selectedSeries: Optional[conint(ge=0, le=2147483647)] = 0


class DatagridPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
