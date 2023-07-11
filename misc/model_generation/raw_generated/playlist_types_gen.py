# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field


class Type(Enum):
    dashboard_by_uid = 'dashboard_by_uid'
    dashboard_by_id = 'dashboard_by_id'
    dashboard_by_tag = 'dashboard_by_tag'


class PlaylistItem(MyBaseModel):
    type: Type = Field(..., description='Type of the item.')
    value: str = Field(
        ...,
        description='Value depends on type and describes the playlist item.\n\n - dashboard_by_id: The value is an internal numerical identifier set by Grafana. This\n is not portable as the numerical identifier is non-deterministic between different instances.\n Will be replaced by dashboard_by_uid in the future. (deprecated)\n - dashboard_by_tag: The value is a tag which is set on any number of dashboards. All\n dashboards behind the tag will be added to the playlist.\n - dashboard_by_uid: The value is the dashboard UID',
    )
    title: Optional[str] = Field(
        None,
        description='Title is an unused property -- it will be removed in the future',
    )


class FieldKubeObjectMetadata(MyBaseModel):
    uid: str
    creationTimestamp: datetime
    deletionTimestamp: Optional[datetime] = None
    finalizers: List[str]
    resourceVersion: str
    labels: Dict[str, str]


class Metadata(FieldKubeObjectMetadata):
    updateTimestamp: datetime
    createdBy: str
    updatedBy: str
    extraFields: Dict[str, Any] = Field(
        ...,
        description='extraFields is reserved for any fields that are pulled from the API server metadata but do not have concrete fields in the CUE metadata',
    )


class Spec(MyBaseModel):
    uid: str = Field(
        ...,
        description='Unique playlist identifier. Generated on creation, either by the\ncreator of the playlist of by the application.',
    )
    name: str = Field(..., description='Name of the playlist.')
    interval: Optional[str] = Field(
        '5m',
        description='Interval sets the time between switching views in a playlist.\nFIXME: Is this based on a standardized format or what options are available? Can datemath be used?',
    )
    items: Optional[List[PlaylistItem]] = Field(
        None,
        description='The ordered list of items that the playlist will iterate over.\nFIXME! This should not be optional, but changing it makes the godegen awkward',
    )


class State(Enum):
    success = 'success'
    in_progress = 'in_progress'
    failed = 'failed'


class JoinSchemaStatusOperatorState(MyBaseModel):
    lastEvaluation: str = Field(
        ..., description='lastEvaluation is the ResourceVersion last evaluated'
    )
    state: State = Field(
        ...,
        description='state describes the state of the lastEvaluation.\nIt is limited to three possible states for machine evaluation.',
    )
    descriptiveState: Optional[str] = Field(
        None,
        description='descriptiveState is an optional more descriptive state field which has no requirements on format',
    )
    details: Optional[Dict[str, Any]] = Field(
        None,
        description='details contains any extra information that is operator-specific',
    )


class StatusOperatorState(MyBaseModel):
    lastEvaluation: str = Field(
        ..., description='lastEvaluation is the ResourceVersion last evaluated'
    )
    state: State = Field(
        ...,
        description='state describes the state of the lastEvaluation.\nIt is limited to three possible states for machine evaluation.',
    )
    descriptiveState: Optional[str] = Field(
        None,
        description='descriptiveState is an optional more descriptive state field which has no requirements on format',
    )
    details: Optional[Dict[str, Any]] = Field(
        None,
        description='details contains any extra information that is operator-specific',
    )


class Status(MyBaseModel):
    operatorStates: Optional[Dict[str, JoinSchemaStatusOperatorState]] = Field(
        None,
        description='operatorStates is a map of operator ID to operator state evaluations.\nAny operator which consumes this kind SHOULD add its state evaluation information to this field.',
    )
    additionalFields: Dict[str, Any] = Field(
        ..., description='additionalFields is reserved for future use'
    )


class Playlist(MyBaseModel):
    metadata: Metadata = Field(
        ...,
        description='metadata contains embedded CommonMetadata and can be extended with custom string fields\nTODO: use CommonMetadata instead of redefining here; currently needs to be defined here\nwithout external reference as using the CommonMetadata reference breaks thema codegen.',
    )
    spec: Spec
    status: Status
