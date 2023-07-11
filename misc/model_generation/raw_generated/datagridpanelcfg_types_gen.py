# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, conint


class PanelOptions(BaseModel):
    selectedSeries: Optional[conint(ge=0, le=2147483647)] = 0


class DatagridPanelCfg(BaseModel):
    PanelOptions: PanelOptions
