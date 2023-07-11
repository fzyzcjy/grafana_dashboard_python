# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from pydantic import BaseModel, Field


class PanelOptions(BaseModel):
    labels: str = Field(
        ..., description='Comma-separated list of values used to filter alert results'
    )
    alertmanager: str = Field(
        ..., description='Name of the alertmanager used as a source for alerts'
    )
    expandAll: bool = Field(..., description='Expand all alert groups by default')


class AlertGroupsPanelCfg(BaseModel):
    PanelOptions: PanelOptions
