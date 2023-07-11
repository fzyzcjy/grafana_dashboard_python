# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from grafana_dashboard.extracted_generated_common_models import *

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field, conint, constr


class LibraryElementDTOMetaUser(MyBaseModel):
    id: int
    name: str
    avatarUrl: str


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


class LibraryElementDTOMeta(MyBaseModel):
    folderName: str
    folderUid: str
    connectedDashboards: int
    created: datetime
    updated: datetime
    createdBy: LibraryElementDTOMetaUser
    updatedBy: LibraryElementDTOMetaUser


class Spec(MyBaseModel):
    folderUid: Optional[str] = Field(None, description='Folder UID')
    uid: str = Field(..., description='Library element UID')
    name: constr(min_length=1) = Field(
        ..., description='Panel name (also saved in the model)'
    )
    description: Optional[str] = Field(None, description='Panel description')
    type: constr(min_length=1) = Field(
        ..., description='The panel type (from inside the model)'
    )
    schemaVersion: Optional[conint(ge=0, le=65535)] = Field(
        None, description='Dashboard version when this was saved (zero if unknown)'
    )
    version: int = Field(
        ...,
        description='panel version, incremented each time the dashboard is updated.',
    )
    model: Dict[str, Any] = Field(
        ...,
        description="TODO: should be the same panel schema defined in dashboard\nTypescript: Omit<Panel, 'gridPos' | 'id' | 'libraryPanel'>;",
    )
    meta: Optional[LibraryElementDTOMeta] = None


class Status(MyBaseModel):
    operatorStates: Optional[Dict[str, JoinSchemaStatusOperatorState]] = Field(
        None,
        description='operatorStates is a map of operator ID to operator state evaluations.\nAny operator which consumes this kind SHOULD add its state evaluation information to this field.',
    )
    additionalFields: Dict[str, Any] = Field(
        ..., description='additionalFields is reserved for future use'
    )


class Librarypanel(MyBaseModel):
    metadata: Metadata = Field(
        ...,
        description='metadata contains embedded CommonMetadata and can be extended with custom string fields\nTODO: use CommonMetadata instead of redefining here; currently needs to be defined here\nwithout external reference as using the CommonMetadata reference breaks thema codegen.',
    )
    spec: Spec
    status: Status
