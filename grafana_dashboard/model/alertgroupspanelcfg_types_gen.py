# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND


from pydantic import Field

from grafana_dashboard.utils import MyBaseModel


class PanelOptions(MyBaseModel):
    labels: str = Field(
        ..., description='Comma-separated list of values used to filter alert results'
    )
    alertmanager: str = Field(
        ..., description='Name of the alertmanager used as a source for alerts'
    )
    expandAll: bool = Field(..., description='Expand all alert groups by default')


class AlertGroupsPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
