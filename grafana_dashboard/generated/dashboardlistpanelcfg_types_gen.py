# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class PanelOptions(BaseModel):
    keepTime: bool
    includeVars: bool
    showStarred: bool
    showRecentlyViewed: bool
    showSearch: bool
    showHeadings: bool
    maxItems: int
    query: str
    folderId: Optional[int] = None
    tags: List[str]


class DashboardListPanelCfg(BaseModel):
    PanelOptions: PanelOptions
