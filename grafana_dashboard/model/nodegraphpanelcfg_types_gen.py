# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND


from typing import List, Optional

from pydantic import Field

from grafana_dashboard.utils import MyBaseModel


class ArcOption(MyBaseModel):
    field: Optional[str] = Field(
        None,
        description='Field from which to get the value. Values should be less than 1, representing fraction of a circle.',
    )
    color: Optional[str] = Field(None, description='The color of the arc.')


class EdgeOptions(MyBaseModel):
    mainStatUnit: Optional[str] = Field(
        None,
        description='Unit for the main stat to override what ever is set in the data frame.',
    )
    secondaryStatUnit: Optional[str] = Field(
        None,
        description='Unit for the secondary stat to override what ever is set in the data frame.',
    )


class NodeOptions(MyBaseModel):
    mainStatUnit: Optional[str] = Field(
        None,
        description='Unit for the main stat to override what ever is set in the data frame.',
    )
    secondaryStatUnit: Optional[str] = Field(
        None,
        description='Unit for the secondary stat to override what ever is set in the data frame.',
    )
    arcs: Optional[List[ArcOption]] = Field(
        None,
        description='Define which fields are shown as part of the node arc (colored circle around the node).',
    )


class PanelOptions(MyBaseModel):
    nodes: Optional[NodeOptions] = None
    edges: Optional[EdgeOptions] = None


class NodeGraphPanelCfg(MyBaseModel):
    ArcOption: ArcOption
    NodeOptions: NodeOptions
    EdgeOptions: EdgeOptions
    PanelOptions: PanelOptions
