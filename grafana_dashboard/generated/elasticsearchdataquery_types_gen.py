# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class BucketAggregationType(Enum):
    terms = 'terms'
    filters = 'filters'
    geohash_grid = 'geohash_grid'
    date_histogram = 'date_histogram'
    histogram = 'histogram'
    nested = 'nested'


class Settings2(BaseModel):
    format: Optional[str] = None


class DataQuery(BaseModel):
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


class DateHistogramSettings(BaseModel):
    interval: Optional[str] = None
    min_doc_count: Optional[str] = None
    trimEdges: Optional[str] = None
    offset: Optional[str] = None
    timeZone: Optional[str] = None


class Settings3(BaseModel):
    unit: Optional[str] = None


class ExtendedStatMetaType(Enum):
    avg = 'avg'
    min = 'min'
    max = 'max'
    sum = 'sum'
    count = 'count'
    std_deviation = 'std_deviation'
    std_deviation_bounds_upper = 'std_deviation_bounds_upper'
    std_deviation_bounds_lower = 'std_deviation_bounds_lower'


class Filter(BaseModel):
    query: str
    label: str


class FiltersSettings(BaseModel):
    filters: Optional[List[Filter]] = None


class GeoHashGridSettings(BaseModel):
    precision: Optional[str] = None


class HistogramSettings(BaseModel):
    interval: Optional[str] = None
    min_doc_count: Optional[str] = None


class InlineScriptItem(BaseModel):
    inline: Optional[str] = None


class InlineScript(BaseModel):
    __root__: Union[str, InlineScriptItem]


class Settings5(BaseModel):
    limit: Optional[str] = None


class Settings6(BaseModel):
    script: Optional[InlineScript] = None
    missing: Optional[str] = None


class MetricAggregationType(Enum):
    count = 'count'
    avg = 'avg'
    sum = 'sum'
    min = 'min'
    max = 'max'
    extended_stats = 'extended_stats'
    percentiles = 'percentiles'
    cardinality = 'cardinality'
    raw_document = 'raw_document'
    raw_data = 'raw_data'
    logs = 'logs'
    rate = 'rate'
    top_metrics = 'top_metrics'
    moving_avg = 'moving_avg'
    moving_fn = 'moving_fn'
    derivative = 'derivative'
    serial_diff = 'serial_diff'
    cumulative_sum = 'cumulative_sum'
    bucket_script = 'bucket_script'


class Settings7(BaseModel):
    script: Optional[InlineScript] = None


class Settings8(BaseModel):
    missing: Optional[str] = None


class Settings9(BaseModel):
    script: Optional[InlineScript] = None
    missing: Optional[str] = None


class Settings10(BaseModel):
    alpha: Optional[str] = None


class Settings11(BaseModel):
    alpha: Optional[str] = None
    beta: Optional[str] = None


class Settings12(BaseModel):
    alpha: Optional[str] = None
    beta: Optional[str] = None
    gamma: Optional[str] = None
    period: Optional[str] = None
    pad: Optional[bool] = None


class MovingAverageModel(Enum):
    simple = 'simple'
    linear = 'linear'
    ewma = 'ewma'
    holt = 'holt'
    holt_winters = 'holt_winters'


class MovingAverageModelOption(BaseModel):
    label: str
    value: MovingAverageModel


class Settings13(BaseModel):
    window: Optional[str] = None
    script: Optional[InlineScript] = None
    shift: Optional[str] = None


class Settings14(BaseModel):
    script: Optional[InlineScript] = None
    missing: Optional[str] = None
    percents: Optional[List[str]] = None


class PipelineMetricAggregationType(Enum):
    moving_avg = 'moving_avg'
    moving_fn = 'moving_fn'
    derivative = 'derivative'
    serial_diff = 'serial_diff'
    cumulative_sum = 'cumulative_sum'
    bucket_script = 'bucket_script'


class PipelineVariable(BaseModel):
    name: str
    pipelineAgg: str


class Settings15(BaseModel):
    unit: Optional[str] = None
    mode: Optional[str] = None


class Settings16(BaseModel):
    size: Optional[str] = None


class Settings18(BaseModel):
    lag: Optional[str] = None


class Settings19(BaseModel):
    script: Optional[InlineScript] = None
    missing: Optional[str] = None


class TermsOrder(Enum):
    desc = 'desc'
    asc = 'asc'


class TermsSettings(BaseModel):
    order: Optional[TermsOrder] = None
    size: Optional[str] = None
    min_doc_count: Optional[str] = None
    orderBy: Optional[str] = None
    missing: Optional[str] = None


class Settings20(BaseModel):
    order: Optional[str] = None
    orderBy: Optional[str] = None
    metrics: Optional[List[str]] = None


class Settings21(BaseModel):
    precision_threshold: Optional[str] = None
    missing: Optional[str] = None


class Settings(BaseModel):
    script: Optional[InlineScript] = None
    missing: Optional[str] = None


class BaseBucketAggregation(BaseModel):
    id: str
    type: BucketAggregationType
    settings: Optional[Any] = None


class BaseMetricAggregation(BaseModel):
    type: MetricAggregationType
    id: str
    hide: Optional[bool] = None


class BaseMovingAverageModelSettings(BaseModel):
    model: MovingAverageModel
    window: str
    predict: str


class BucketAggregationWithField(BaseBucketAggregation):
    field: Optional[str] = None


class Settings1(BaseModel):
    script: Optional[InlineScript] = None


class Count(BaseMetricAggregation):
    type: MetricAggregationType


class DateHistogram(BucketAggregationWithField):
    type: BucketAggregationType
    settings: Optional[DateHistogramSettings] = None


class ExtendedStat(BaseModel):
    label: str
    value: ExtendedStatMetaType


class Settings4(BaseModel):
    script: Optional[InlineScript] = None
    missing: Optional[str] = None
    sigma: Optional[str] = None


class Filters(BaseBucketAggregation):
    type: BucketAggregationType
    settings: Optional[FiltersSettings] = None


class GeoHashGrid(BucketAggregationWithField):
    type: BucketAggregationType
    settings: Optional[GeoHashGridSettings] = None


class Histogram(BucketAggregationWithField):
    type: BucketAggregationType
    settings: Optional[HistogramSettings] = None


class Logs(BaseMetricAggregation):
    type: MetricAggregationType
    settings: Optional[Settings5] = None


class MetricAggregationWithField(BaseMetricAggregation):
    field: Optional[str] = None


class MetricAggregationWithInlineScript(BaseMetricAggregation):
    settings: Optional[Settings7] = None


class MetricAggregationWithMissingSupport(BaseMetricAggregation):
    settings: Optional[Settings8] = None


class Min(MetricAggregationWithField, MetricAggregationWithInlineScript):
    type: MetricAggregationType
    settings: Optional[Settings9] = None


class MovingAverageEWMAModelSettings(BaseMovingAverageModelSettings):
    model: MovingAverageModel
    settings: Optional[Settings10] = None
    minimize: bool


class MovingAverageHoltModelSettings(BaseMovingAverageModelSettings):
    model: MovingAverageModel
    settings: Settings11
    minimize: bool


class MovingAverageHoltWintersModelSettings(BaseMovingAverageModelSettings):
    model: MovingAverageModel
    settings: Settings12
    minimize: bool


class MovingAverageLinearModelSettings(BaseMovingAverageModelSettings):
    model: MovingAverageModel


class MovingAverageSimpleModelSettings(BaseMovingAverageModelSettings):
    model: MovingAverageModel


class Nested(BucketAggregationWithField):
    type: BucketAggregationType
    settings: Optional[Dict[str, Any]] = None


class Percentiles(MetricAggregationWithField, MetricAggregationWithInlineScript):
    type: MetricAggregationType
    settings: Optional[Settings14] = None


class PipelineMetricAggregationWithMultipleBucketPaths(BaseMetricAggregation):
    pipelineVariables: Optional[List[PipelineVariable]] = None


class Rate(MetricAggregationWithField):
    type: MetricAggregationType
    settings: Optional[Settings15] = None


class RawData(BaseMetricAggregation):
    type: MetricAggregationType
    settings: Optional[Settings16] = None


class RawDocument(BaseMetricAggregation):
    type: MetricAggregationType
    settings: Optional[Settings16] = None


class Sum(MetricAggregationWithField, MetricAggregationWithInlineScript):
    type: MetricAggregationType
    settings: Optional[Settings19] = None


class Terms(BucketAggregationWithField):
    type: BucketAggregationType
    settings: Optional[TermsSettings] = None


class TopMetrics(BaseMetricAggregation):
    type: MetricAggregationType
    settings: Optional[Settings20] = None


class UniqueCount(MetricAggregationWithField):
    type: MetricAggregationType
    settings: Optional[Settings21] = None


class Average(
    MetricAggregationWithField,
    MetricAggregationWithMissingSupport,
    MetricAggregationWithInlineScript,
):
    type: MetricAggregationType
    settings: Optional[Settings] = None


class BasePipelineMetricAggregation(MetricAggregationWithField):
    pipelineAgg: Optional[str] = None
    type: PipelineMetricAggregationType


class BucketAggregation(BaseModel):
    __root__: Union[DateHistogram, Histogram, Terms, Filters, GeoHashGrid, Nested]


class BucketScript(PipelineMetricAggregationWithMultipleBucketPaths):
    type: PipelineMetricAggregationType
    settings: Optional[Settings1] = None


class CumulativeSum(BasePipelineMetricAggregation):
    type: PipelineMetricAggregationType
    settings: Optional[Settings2] = None


class Derivative(BasePipelineMetricAggregation):
    type: PipelineMetricAggregationType
    settings: Optional[Settings3] = None


class ExtendedStats(MetricAggregationWithField, MetricAggregationWithInlineScript):
    type: MetricAggregationType
    settings: Optional[Settings4] = None
    meta: Optional[Dict[str, Any]] = None


class Max(MetricAggregationWithField, MetricAggregationWithInlineScript):
    type: MetricAggregationType
    settings: Optional[Settings6] = None


class MovingAverage(BasePipelineMetricAggregation):
    type: PipelineMetricAggregationType
    settings: Optional[Dict[str, Any]] = None


class MovingFunction(BasePipelineMetricAggregation):
    type: PipelineMetricAggregationType
    settings: Optional[Settings13] = None


class PipelineMetricAggregation(BaseModel):
    __root__: Union[MovingAverage, Derivative, CumulativeSum, BucketScript]


class SerialDiff(BasePipelineMetricAggregation):
    type: PipelineMetricAggregationType
    settings: Optional[Settings18] = None


class MetricAggregationWithSettings(BaseModel):
    __root__: Union[
        BucketScript,
        CumulativeSum,
        Derivative,
        SerialDiff,
        RawData,
        RawDocument,
        UniqueCount,
        Percentiles,
        ExtendedStats,
        Min,
        Max,
        Sum,
        Average,
        MovingAverage,
        MovingFunction,
        Logs,
        Rate,
        TopMetrics,
    ]


class MetricAggregation(BaseModel):
    __root__: Union[Count, PipelineMetricAggregation, MetricAggregationWithSettings]


class ElasticsearchDataQuery(DataQuery):
    alias: Optional[str] = Field(None, description='Alias pattern')
    query: Optional[str] = Field(None, description='Lucene query')
    timeField: Optional[str] = Field(None, description='Name of time field')
    bucketAggs: Optional[List[BucketAggregation]] = Field(
        None, description='List of bucket aggregations'
    )
    metrics: Optional[List[MetricAggregation]] = Field(
        None, description='List of metric aggregations'
    )
