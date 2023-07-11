# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND


from typing import Optional

from pydantic import Field

from grafana_dashboard.utils import MyBaseModel


class PanelOptions(MyBaseModel):
    feedUrl: Optional[str] = Field(
        None, description='empty/missing will default to grafana blog'
    )
    showImage: Optional[bool] = True


class NewsPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
