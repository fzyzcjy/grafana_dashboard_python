# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class OrgRole(Enum):
    Admin = 'Admin'
    Editor = 'Editor'
    Viewer = 'Viewer'


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
    id: int = Field(
        ...,
        description='ID is the unique identifier of the service account in the database.',
    )
    orgId: int = Field(
        ...,
        description='OrgId is the ID of an organisation the service account belongs to.',
    )
    name: str = Field(..., description='Name of the service account.')
    login: str = Field(..., description='Login of the service account.')
    isDisabled: bool = Field(
        ..., description='IsDisabled indicates if the service account is disabled.'
    )
    role: OrgRole
    tokens: int = Field(
        ...,
        description='Tokens is the number of active tokens for the service account.\nTokens are used to authenticate the service account against Grafana.',
    )
    avatarUrl: str = Field(
        ...,
        description="AvatarUrl is the service account's avatar URL. It allows the frontend to display a picture in front\nof the service account.",
    )
    accessControl: Optional[Dict[str, bool]] = Field(
        None, description='AccessControl metadata associated with a given resource.'
    )
    teams: Optional[List[str]] = Field(
        None, description='Teams is a list of teams the service account belongs to.'
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


class Serviceaccount(BaseModel):
    metadata: Metadata = Field(
        ...,
        description='metadata contains embedded CommonMetadata and can be extended with custom string fields\nTODO: use CommonMetadata instead of redefining here; currently needs to be defined here\nwithout external reference as using the CommonMetadata reference breaks thema codegen.',
    )
    spec: Spec
    status: Status
