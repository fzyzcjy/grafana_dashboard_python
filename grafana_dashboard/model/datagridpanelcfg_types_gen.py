# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from grafana_dashboard.extracted_generated_common_models import *

from __future__ import annotations

from typing import Optional

from grafana_dashboard.utils import MyBaseModel
from pydantic import conint


class PanelOptions(MyBaseModel):
    selectedSeries: Optional[conint(ge=0, le=2147483647)] = 0


class DatagridPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
