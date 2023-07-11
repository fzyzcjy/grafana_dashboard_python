# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from typing import List

from pydantic import BaseModel, conint


class PanelOptions(BaseModel):
    onlyFromThisDashboard: bool
    onlyInTimeRange: bool
    tags: List[str]
    limit: conint(ge=0, le=4294967295)
    showUser: bool
    showTime: bool
    showTags: bool
    navigateToPanel: bool
    navigateBefore: str
    navigateAfter: str


class AnnotationsListPanelCfg(BaseModel):
    PanelOptions: PanelOptions
