# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class FieldKubeObjectMetadata(BaseModel):
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


class Spec(BaseModel):
    uid: str = Field(..., description='Unique public dashboard identifier')
    dashboardUid: str = Field(
        ...,
        description='Dashboard unique identifier referenced by this public dashboard',
    )
    accessToken: Optional[str] = Field(None, description='Unique public access token')
    isEnabled: bool = Field(
        ..., description='Flag that indicates if the public dashboard is enabled'
    )
    annotationsEnabled: bool = Field(
        ..., description='Flag that indicates if annotations are enabled'
    )
    timeSelectionEnabled: bool = Field(
        ..., description='Flag that indicates if the time range picker is enabled'
    )


class State(Enum):
    success = 'success'
    in_progress = 'in_progress'
    failed = 'failed'


class JoinSchemaStatusOperatorState(BaseModel):
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


class StatusOperatorState(BaseModel):
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


class Status(BaseModel):
    operatorStates: Optional[Dict[str, JoinSchemaStatusOperatorState]] = Field(
        None,
        description='operatorStates is a map of operator ID to operator state evaluations.\nAny operator which consumes this kind SHOULD add its state evaluation information to this field.',
    )
    additionalFields: Dict[str, Any] = Field(
        ..., description='additionalFields is reserved for future use'
    )


class Publicdashboard(BaseModel):
    metadata: Metadata = Field(
        ...,
        description='metadata contains embedded CommonMetadata and can be extended with custom string fields\nTODO: use CommonMetadata instead of redefining here; currently needs to be defined here\nwithout external reference as using the CommonMetadata reference breaks thema codegen.',
    )
    spec: Spec
    status: Status
