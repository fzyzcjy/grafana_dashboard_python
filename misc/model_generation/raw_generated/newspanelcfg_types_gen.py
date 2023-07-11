# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class PanelOptions(BaseModel):
    feedUrl: Optional[str] = Field(
        None, description='empty/missing will default to grafana blog'
    )
    showImage: Optional[bool] = True


class NewsPanelCfg(BaseModel):
    PanelOptions: PanelOptions
