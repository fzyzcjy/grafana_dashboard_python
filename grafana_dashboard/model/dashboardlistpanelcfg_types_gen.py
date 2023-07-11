# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from typing import List, Optional

from grafana_dashboard.utils import MyBaseModel


class PanelOptions(MyBaseModel):
    keepTime: Optional[bool] = False
    includeVars: Optional[bool] = False
    showStarred: Optional[bool] = True
    showRecentlyViewed: Optional[bool] = False
    showSearch: Optional[bool] = False
    showHeadings: Optional[bool] = True
    maxItems: Optional[int] = 10
    query: Optional[str] = ''
    folderId: Optional[int] = None
    tags: List[str]


class DashboardListPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
