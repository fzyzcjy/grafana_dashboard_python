# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field, confloat


class CSVWave(MyBaseModel):
    timeStep: Optional[int] = None
    name: Optional[str] = None
    valuesCSV: Optional[str] = None
    labels: Optional[str] = None


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


class Type(Enum):
    random = 'random'
    response = 'response'
    random_edges = 'random edges'


class NodesQuery(MyBaseModel):
    type: Optional[Type] = None
    count: Optional[int] = None


class PulseWaveQuery(MyBaseModel):
    timeStep: Optional[int] = None
    onCount: Optional[int] = None
    offCount: Optional[int] = None
    onValue: Optional[float] = None
    offValue: Optional[float] = None


class Scenario(MyBaseModel):
    id: str
    name: str
    stringInput: str
    description: Optional[str] = None
    hideAliasField: Optional[bool] = None


class Key(MyBaseModel):
    type: str
    tick: float
    uid: Optional[str] = None


class SimulationQuery(MyBaseModel):
    key: Key
    config: Optional[Dict[str, Any]] = None
    stream: Optional[bool] = None
    last: Optional[bool] = None


class Type1(Enum):
    signal = 'signal'
    logs = 'logs'
    fetch = 'fetch'


class StreamingQuery(MyBaseModel):
    type: Type1
    speed: int
    spread: int
    noise: int
    bands: Optional[int] = None
    url: Optional[str] = None


class ErrorType(Enum):
    server_panic = 'server_panic'
    frontend_exception = 'frontend_exception'
    frontend_observable = 'frontend_observable'


class TestDataQueryType(Enum):
    random_walk = 'random_walk'
    slow_query = 'slow_query'
    random_walk_with_error = 'random_walk_with_error'
    random_walk_table = 'random_walk_table'
    exponential_heatmap_bucket_data = 'exponential_heatmap_bucket_data'
    linear_heatmap_bucket_data = 'linear_heatmap_bucket_data'
    no_data_points = 'no_data_points'
    datapoints_outside_range = 'datapoints_outside_range'
    csv_metric_values = 'csv_metric_values'
    predictable_pulse = 'predictable_pulse'
    predictable_csv_wave = 'predictable_csv_wave'
    streaming_client = 'streaming_client'
    simulation = 'simulation'
    usa = 'usa'
    live = 'live'
    grafana_api = 'grafana_api'
    arrow = 'arrow'
    annotations = 'annotations'
    table_static = 'table_static'
    server_error_500 = 'server_error_500'
    logs = 'logs'
    node_graph = 'node_graph'
    flame_graph = 'flame_graph'
    raw_frame = 'raw_frame'
    csv_file = 'csv_file'
    csv_content = 'csv_content'
    trace = 'trace'
    manual_entry = 'manual_entry'
    variables_query = 'variables-query'


class USAQuery(MyBaseModel):
    mode: Optional[str] = None
    period: Optional[str] = None
    fields: Optional[List[str]] = None
    states: Optional[List[str]] = None


class TestDataDataQuery(DataQuery):
    alias: Optional[str] = None
    scenarioId: Optional[TestDataQueryType] = None
    stringInput: Optional[str] = None
    stream: Optional[StreamingQuery] = None
    pulseWave: Optional[PulseWaveQuery] = None
    sim: Optional[SimulationQuery] = None
    csvWave: Optional[List[CSVWave]] = None
    labels: Optional[str] = None
    lines: Optional[int] = None
    levelColumn: Optional[bool] = None
    channel: Optional[str] = None
    nodes: Optional[NodesQuery] = None
    csvFileName: Optional[str] = None
    csvContent: Optional[str] = None
    rawFrameContent: Optional[str] = None
    seriesCount: Optional[int] = None
    usa: Optional[USAQuery] = None
    errorType: Optional[ErrorType] = None
    spanCount: Optional[int] = None
    points: Optional[
        List[
            List[
                Union[str, confloat(ge=-9.223372036854776e18, le=9.223372036854776e18)]
            ]
        ]
    ] = None
