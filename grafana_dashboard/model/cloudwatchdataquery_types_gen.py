# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from grafana_dashboard.extracted_generated_common_models import *

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field, confloat


class CloudWatchDataQuery(MyBaseModel):
    pass


class CloudWatchQueryMode(Enum):
    Metrics = 'Metrics'
    Logs = 'Logs'
    Annotations = 'Annotations'


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


class Dimensions(MyBaseModel):
    __root__: Optional[Dict[str, Union[str, List[str]]]] = None


class LogGroup(MyBaseModel):
    arn: str = Field(..., description='ARN of the log group')
    name: str = Field(..., description='Name of the log group')
    accountId: Optional[str] = Field(None, description='AccountId of the log group')
    accountLabel: Optional[str] = Field(None, description='Label of the log group')


class MetricEditorMode(Enum):
    integer_0 = 0
    integer_1 = 1


class MetricQueryType(Enum):
    integer_0 = 0
    integer_1 = 1


class MetricStat(MyBaseModel):
    region: str = Field(..., description='AWS region to query for the metric')
    namespace: str = Field(
        ...,
        description='A namespace is a container for CloudWatch metrics. Metrics in different namespaces are isolated from each other, so that metrics from different applications are not mistakenly aggregated into the same statistics. For example, Amazon EC2 uses the AWS/EC2 namespace.',
    )
    metricName: Optional[str] = Field(None, description='Name of the metric')
    dimensions: Optional[Dimensions] = None
    matchExact: Optional[bool] = Field(
        None,
        description='Only show metrics that exactly match all defined dimension names.',
    )
    period: Optional[str] = Field(
        None,
        description="The length of time associated with a specific Amazon CloudWatch statistic. Can be specified by a number of seconds, 'auto', or as a duration string e.g. '15m' being 15 minutes",
    )
    accountId: Optional[str] = Field(
        None,
        description='The ID of the AWS account to query for the metric, specifying `all` will query all accounts that the monitoring account is permitted to query.',
    )
    statistic: Optional[str] = Field(
        None,
        description='Metric data aggregations over specified periods of time. For detailed definitions of the statistics supported by CloudWatch, see https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html.',
    )
    statistics: Optional[List[str]] = Field(
        None, description='@deprecated use statistic'
    )


class Type(Enum):
    and_ = 'and'
    or_ = 'or'


class QueryEditorExpressionType(Enum):
    property = 'property'
    operator = 'operator'
    or_ = 'or'
    and_ = 'and'
    groupBy = 'groupBy'
    function = 'function'
    functionParameter = 'functionParameter'


class QueryEditorFunctionParameterExpression(MyBaseModel):
    type: QueryEditorExpressionType
    name: Optional[str] = None


class QueryEditorOperatorType(MyBaseModel):
    __root__: Union[
        str, bool, confloat(ge=-9.223372036854776e18, le=9.223372036854776e18)
    ]


class QueryEditorOperatorValueType(MyBaseModel):
    __root__: Union[
        str,
        bool,
        confloat(ge=-9.223372036854776e18, le=9.223372036854776e18),
        List[QueryEditorOperatorType],
    ]


class QueryEditorPropertyType(Enum):
    string = 'string'


class CloudWatchAnnotationQuery(DataQuery, MetricStat):
    queryMode: CloudWatchQueryMode
    prefixMatching: Optional[bool] = Field(
        None,
        description='Enable matching on the prefix of the action name or alarm name, specify the prefixes with actionPrefix and/or alarmNamePrefix',
    )
    actionPrefix: Optional[str] = Field(
        None,
        description='Use this parameter to filter the results of the operation to only those alarms\nthat use a certain alarm action. For example, you could specify the ARN of\nan SNS topic to find all alarms that send notifications to that topic.\ne.g. `arn:aws:sns:us-east-1:123456789012:my-app-` would match `arn:aws:sns:us-east-1:123456789012:my-app-action`\nbut not match `arn:aws:sns:us-east-1:123456789012:your-app-action`',
    )
    alarmNamePrefix: Optional[str] = Field(
        None,
        description='An alarm name prefix. If you specify this parameter, you receive information\nabout all alarms that have names that start with this prefix.\ne.g. `my-team-service-` would match `my-team-service-high-cpu` but not match `your-team-service-high-cpu`',
    )


class CloudWatchLogsQuery(DataQuery):
    queryMode: CloudWatchQueryMode
    id: str
    region: str = Field(..., description='AWS region to query for the logs')
    expression: Optional[str] = Field(
        None, description='The CloudWatch Logs Insights query to execute'
    )
    statsGroups: Optional[List[str]] = Field(
        None,
        description='Fields to group the results by, this field is automatically populated whenever the query is updated',
    )
    logGroups: Optional[List[LogGroup]] = Field(None, description='Log groups to query')
    logGroupNames: Optional[List[str]] = Field(
        None, description='@deprecated use logGroups'
    )


class QueryEditorFunctionExpression(MyBaseModel):
    type: QueryEditorExpressionType
    name: Optional[str] = None
    parameters: Optional[List[QueryEditorFunctionParameterExpression]] = None


class QueryEditorOperator(MyBaseModel):
    name: Optional[str] = None
    value: Optional[
        Union[
            str,
            bool,
            confloat(ge=-9.223372036854776e18, le=9.223372036854776e18),
            List[QueryEditorOperatorType],
        ]
    ] = None


class QueryEditorProperty(MyBaseModel):
    type: QueryEditorPropertyType
    name: Optional[str] = None


class QueryEditorPropertyExpression(MyBaseModel):
    type: QueryEditorExpressionType
    property: QueryEditorProperty


class QueryEditorGroupByExpression(MyBaseModel):
    type: QueryEditorExpressionType
    property: QueryEditorProperty


class QueryEditorOperatorExpression(MyBaseModel):
    type: QueryEditorExpressionType
    property: QueryEditorProperty
    operator: QueryEditorOperator


class CloudWatchMetricsQuery(DataQuery, MetricStat):
    queryMode: Optional[CloudWatchQueryMode] = None
    metricQueryType: Optional[MetricQueryType] = None
    metricEditorMode: Optional[MetricEditorMode] = None
    id: str = Field(
        ...,
        description='ID can be used to reference other queries in math expressions. The ID can include numbers, letters, and underscore, and must start with a lowercase letter.',
    )
    alias: Optional[str] = Field(
        None, description='Deprecated: use label\n@deprecated use label'
    )
    label: Optional[str] = Field(
        None,
        description='Change the time series legend names using dynamic labels. See https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html for more details.',
    )
    expression: Optional[str] = Field(None, description='Math expression query')
    sqlExpression: Optional[str] = Field(
        None,
        description='When the metric query type is `metricQueryType` is set to `Query`, this field is used to specify the query string.',
    )
    sql: Optional[SQLExpression] = None


class QueryEditorArrayExpression(MyBaseModel):
    type: Type
    expressions: List[QueryEditorExpression]


class QueryEditorExpression(MyBaseModel):
    __root__: Union[
        QueryEditorArrayExpression,
        QueryEditorPropertyExpression,
        QueryEditorGroupByExpression,
        QueryEditorFunctionExpression,
        QueryEditorFunctionParameterExpression,
        QueryEditorOperatorExpression,
    ]


class SQLExpression(MyBaseModel):
    select: Optional[QueryEditorFunctionExpression] = None
    from_: Optional[
        Union[QueryEditorPropertyExpression, QueryEditorFunctionExpression]
    ] = Field(None, alias='from', description='FROM part of the SQL expression')
    where: Optional[QueryEditorArrayExpression] = None
    groupBy: Optional[QueryEditorArrayExpression] = None
    orderBy: Optional[QueryEditorFunctionExpression] = None
    orderByDirection: Optional[str] = Field(
        None, description='The sort order of the SQL expression, `ASC` or `DESC`'
    )
    limit: Optional[int] = Field(None, description='LIMIT part of the SQL expression')


CloudWatchMetricsQuery.update_forward_refs()
QueryEditorArrayExpression.update_forward_refs()
