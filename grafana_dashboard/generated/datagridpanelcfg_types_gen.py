# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from pydantic import BaseModel, conint


class PanelOptions(BaseModel):
    selectedSeries: conint(ge=0, le=2147483647)


class DatagridPanelCfg(BaseModel):
    PanelOptions: PanelOptions
