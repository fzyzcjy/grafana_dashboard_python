# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from grafana_dashboard.extracted_generated_common_models import *

from __future__ import annotations

from typing import Optional

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field


class PanelOptions(MyBaseModel):
    feedUrl: Optional[str] = Field(
        None, description='empty/missing will default to grafana blog'
    )
    showImage: Optional[bool] = True


class NewsPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
