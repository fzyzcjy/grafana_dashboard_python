# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

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


class PromQueryFormat(Enum):
    time_series = 'time_series'
    table = 'table'
    heatmap = 'heatmap'


class QueryEditorMode(Enum):
    code = 'code'
    builder = 'builder'


class PrometheusDataQuery(DataQuery):
    expr: str = Field(
        ...,
        description='The actual expression/query that will be evaluated by Prometheus',
    )
    instant: Optional[bool] = Field(
        None,
        description='Returns only the latest value that Prometheus has scraped for the requested time series',
    )
    range: Optional[bool] = Field(
        None,
        description='Returns a Range vector, comprised of a set of time series containing a range of data points over time for each time series',
    )
    exemplar: Optional[bool] = Field(
        None,
        description='Execute an additional query to identify interesting raw samples relevant for the given expr',
    )
    editorMode: Optional[QueryEditorMode] = None
    format: Optional[PromQueryFormat] = None
    legendFormat: Optional[str] = Field(
        None,
        description='Series name override or template. Ex. {{hostname}} will be replaced with label value for hostname',
    )
    intervalFactor: Optional[float] = Field(
        None,
        description='@deprecated Used to specify how many times to divide max data points by. We use max data points under query options\nSee https://github.com/grafana/grafana/issues/48081',
    )
