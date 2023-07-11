# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from grafana_dashboard.extracted_generated_common_models import *

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field


class DataQuery(MyBaseModel):
    refId: str = Field(
        ...,
        description='A unique identifier for the query within the list of targets.\nIn server side expressions, the refId is used as a variable name to identify results.\nBy default, the UI will assign A->Z; however setting meaningful names may be useful.',
    )
    hide: Optional[bool] = Field(
        None,
        description='true if query is disabled (ie should not be returned to the dashboard)\nNote this does not always imply that the query should not be executed since\nthe results from a hidden query may be used as the input to other queries (SSE etc)',
    )
    queryType: Optional[str] = Field(
        None,
        description='Specify the query flavor\nTODO make this required and give it a default',
    )
    datasource: Optional[Any] = Field(
        None,
        description="For mixed data sources the selected datasource is on the query level.\nFor non mixed scenarios this is undefined.\nTODO find a better way to do this ^ that's friendly to schema\nTODO this shouldn't be unknown but DataSourceRef | null",
    )


class TempoDataQuery(MyBaseModel):
    pass


class TempoQueryType(Enum):
    traceql = 'traceql'
    traceqlSearch = 'traceqlSearch'
    search = 'search'
    serviceMap = 'serviceMap'
    upload = 'upload'
    nativeSearch = 'nativeSearch'
    clear = 'clear'


class TraceqlSearchScope(Enum):
    unscoped = 'unscoped'
    resource = 'resource'
    span = 'span'


class TraceqlFilter(MyBaseModel):
    id: str = Field(
        ...,
        description='Uniquely identify the filter, will not be used in the query generation',
    )
    tag: Optional[str] = Field(
        None,
        description='The tag for the search filter, for example: .http.status_code, .service.name, status',
    )
    operator: Optional[str] = Field(
        None,
        description='The operator that connects the tag to the value, for example: =, >, !=, =~',
    )
    value: Optional[Union[str, List[str]]] = Field(
        None, description='The value for the search filter'
    )
    valueType: Optional[str] = Field(
        None,
        description='The type of the value, used for example to check whether we need to wrap the value in quotes when generating the query',
    )
    scope: Optional[TraceqlSearchScope] = None


class TempoQuery(DataQuery):
    query: str = Field(..., description='TraceQL query or trace ID')
    search: Optional[str] = Field(
        None,
        description='Logfmt query to filter traces by their tags. Example: http.status_code=200 error=true',
    )
    serviceName: Optional[str] = Field(None, description='Query traces by service name')
    spanName: Optional[str] = Field(None, description='Query traces by span name')
    minDuration: Optional[str] = Field(
        None,
        description='Define the minimum duration to select traces. Use duration format, for example: 1.2s, 100ms',
    )
    maxDuration: Optional[str] = Field(
        None,
        description='Define the maximum duration to select traces. Use duration format, for example: 1.2s, 100ms',
    )
    serviceMapQuery: Optional[str] = Field(
        None,
        description='Filters to be included in a PromQL query to select data for the service graph. Example: {client="app",service="app"}',
    )
    limit: Optional[int] = Field(
        None,
        description='Defines the maximum number of traces that are returned from Tempo',
    )
    filters: List[TraceqlFilter]
