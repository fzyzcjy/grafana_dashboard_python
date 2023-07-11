# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from grafana_dashboard.extracted_generated_common_models import *

from __future__ import annotations

from enum import Enum
from typing import Any, Optional

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


class LokiQueryDirection(Enum):
    forward = 'forward'
    backward = 'backward'


class LokiQueryType(Enum):
    range = 'range'
    instant = 'instant'
    stream = 'stream'


class QueryEditorMode(Enum):
    code = 'code'
    builder = 'builder'


class SupportingQueryType(Enum):
    logsVolume = 'logsVolume'
    logsSample = 'logsSample'
    dataSample = 'dataSample'


class LokiDataQuery(DataQuery):
    expr: str = Field(..., description='The LogQL query.')
    legendFormat: Optional[str] = Field(
        None, description='Used to override the name of the series.'
    )
    maxLines: Optional[int] = Field(
        None, description='Used to limit the number of log rows returned.'
    )
    resolution: Optional[int] = Field(
        None, description='Used to scale the interval value.'
    )
    editorMode: Optional[QueryEditorMode] = None
    range: Optional[bool] = Field(None, description='@deprecated, now use queryType.')
    instant: Optional[bool] = Field(None, description='@deprecated, now use queryType.')
