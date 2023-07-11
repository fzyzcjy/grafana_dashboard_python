# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND


from typing import List, Optional

from pydantic import conint

from grafana_dashboard.utils import MyBaseModel


class PanelOptions(MyBaseModel):
    onlyFromThisDashboard: Optional[bool] = False
    onlyInTimeRange: Optional[bool] = False
    tags: List[str]
    limit: Optional[conint(ge=0, le=4294967295)] = 10
    showUser: Optional[bool] = True
    showTime: Optional[bool] = True
    showTags: Optional[bool] = True
    navigateToPanel: Optional[bool] = True
    navigateBefore: Optional[str] = '10m'
    navigateAfter: Optional[str] = '10m'


class AnnotationsListPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
