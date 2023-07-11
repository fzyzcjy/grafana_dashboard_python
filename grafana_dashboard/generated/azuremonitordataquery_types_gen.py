# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field


class Kind(Enum):
    AppInsightsGroupByQuery = 'AppInsightsGroupByQuery'


class Kind1(Enum):
    AppInsightsMetricNameQuery = 'AppInsightsMetricNameQuery'


class AzureMetricDimension(BaseModel):
    dimension: Optional[str] = Field(
        None, description='Name of Dimension to be filtered on.'
    )
    operator: Optional[str] = Field(
        None,
        description="String denoting the filter operation. Supports 'eq' - equals,'ne' - not equals, 'sw' - starts with. Note that some dimensions may not support all operators.",
    )
    filters: Optional[List[str]] = Field(
        None, description='Values to match with the filter.'
    )
    filter: Optional[str] = Field(
        None,
        description='@deprecated filter is deprecated in favour of filters to support multiselect.',
    )


class AzureMonitorDataQuery(BaseModel):
    pass


class AzureMonitorResource(BaseModel):
    subscription: Optional[str] = None
    resourceGroup: Optional[str] = None
    resourceName: Optional[str] = None
    metricNamespace: Optional[str] = None
    region: Optional[str] = None


class AzureQueryType(Enum):
    Azure_Monitor = 'Azure Monitor'
    Azure_Log_Analytics = 'Azure Log Analytics'
    Azure_Resource_Graph = 'Azure Resource Graph'
    Azure_Traces = 'Azure Traces'
    Azure_Subscriptions = 'Azure Subscriptions'
    Azure_Resource_Groups = 'Azure Resource Groups'
    Azure_Namespaces = 'Azure Namespaces'
    Azure_Resource_Names = 'Azure Resource Names'
    Azure_Metric_Names = 'Azure Metric Names'
    Azure_Workspaces = 'Azure Workspaces'
    Azure_Regions = 'Azure Regions'
    Grafana_Template_Variable_Function = 'Grafana Template Variable Function'


class AzureResourceGraphQuery(BaseModel):
    query: Optional[str] = Field(
        None, description='Azure Resource Graph KQL query to be executed.'
    )
    resultFormat: Optional[str] = Field(
        None,
        description='Specifies the format results should be returned as. Defaults to table.',
    )


class AzureTracesFilter(BaseModel):
    property: str = Field(
        ..., description='Property name, auto-populated based on available traces.'
    )
    operation: str = Field(
        ..., description='Comparison operator to use. Either equals or not equals.'
    )
    filters: List[str] = Field(..., description='Values to filter by.')


class BaseGrafanaTemplateVariableQuery(BaseModel):
    rawQuery: Optional[str] = None


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


class GrafanaTemplateVariableQueryType(Enum):
    AppInsightsMetricNameQuery = 'AppInsightsMetricNameQuery'
    AppInsightsGroupByQuery = 'AppInsightsGroupByQuery'
    SubscriptionsQuery = 'SubscriptionsQuery'
    ResourceGroupsQuery = 'ResourceGroupsQuery'
    ResourceNamesQuery = 'ResourceNamesQuery'
    MetricNamespaceQuery = 'MetricNamespaceQuery'
    MetricNamesQuery = 'MetricNamesQuery'
    WorkspacesQuery = 'WorkspacesQuery'
    UnknownQuery = 'UnknownQuery'


class Kind2(Enum):
    MetricDefinitionsQuery = 'MetricDefinitionsQuery'


class MetricDefinitionsQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind2
    subscription: str
    resourceGroup: str
    metricNamespace: Optional[str] = None
    resourceName: Optional[str] = None


class Kind3(Enum):
    MetricNamesQuery = 'MetricNamesQuery'


class MetricNamesQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind3
    subscription: str
    resourceGroup: str
    resourceName: str
    metricNamespace: str


class Kind4(Enum):
    MetricNamespaceQuery = 'MetricNamespaceQuery'


class MetricNamespaceQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind4
    subscription: str
    resourceGroup: str
    metricNamespace: Optional[str] = None
    resourceName: Optional[str] = None


class Kind5(Enum):
    ResourceGroupsQuery = 'ResourceGroupsQuery'


class ResourceGroupsQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind5
    subscription: str


class Kind6(Enum):
    ResourceNamesQuery = 'ResourceNamesQuery'


class ResourceNamesQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind6
    subscription: str
    resourceGroup: str
    metricNamespace: str


class ResultFormat(Enum):
    table = 'table'
    time_series = 'time_series'
    trace = 'trace'


class Kind7(Enum):
    SubscriptionsQuery = 'SubscriptionsQuery'


class SubscriptionsQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind7


class Kind8(Enum):
    UnknownQuery = 'UnknownQuery'


class UnknownQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind8


class Kind9(Enum):
    WorkspacesQuery = 'WorkspacesQuery'


class WorkspacesQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind9
    subscription: str


class AppInsightsGroupByQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind
    metricName: str


class AppInsightsMetricNameQuery(BaseGrafanaTemplateVariableQuery):
    kind: Kind1


class AzureLogsQuery(BaseModel):
    query: Optional[str] = Field(None, description='KQL query to be executed.')
    resultFormat: Optional[ResultFormat] = None
    resources: Optional[List[str]] = Field(
        None, description='Array of resource URIs to be queried.'
    )
    workspace: Optional[str] = Field(
        None,
        description='Workspace ID. This was removed in Grafana 8, but remains for backwards compat',
    )
    resource: Optional[str] = Field(
        None, description='@deprecated Use resources instead'
    )


class AzureMetricQuery(BaseModel):
    resources: Optional[List[AzureMonitorResource]] = Field(
        None, description='Array of resource URIs to be queried.'
    )
    metricNamespace: Optional[str] = Field(
        None,
        description="metricNamespace is used as the resource type (or resource namespace).\nIt's usually equal to the target metric namespace. e.g. microsoft.storage/storageaccounts\nKept the name of the variable as metricNamespace to avoid backward incompatibility issues.",
    )
    customNamespace: Optional[str] = Field(
        None,
        description="Used as the value for the metricNamespace property when it's different from the resource namespace.",
    )
    metricName: Optional[str] = Field(
        None,
        description='The metric to query data for within the specified metricNamespace. e.g. UsedCapacity',
    )
    region: Optional[str] = Field(
        None, description='The Azure region containing the resource(s).'
    )
    timeGrain: Optional[str] = Field(
        None,
        description='The granularity of data points to be queried. Defaults to auto.',
    )
    aggregation: Optional[str] = Field(
        None,
        description='The aggregation to be used within the query. Defaults to the primaryAggregationType defined by the metric.',
    )
    dimensionFilters: Optional[List[AzureMetricDimension]] = Field(
        None,
        description='Filters to reduce the set of data returned. Dimensions that can be filtered on are defined by the metric.',
    )
    top: Optional[str] = Field(
        None, description='Maximum number of records to return. Defaults to 10.'
    )
    allowedTimeGrainsMs: Optional[List[int]] = Field(
        None, description='Time grains that are supported by the metric.'
    )
    alias: Optional[str] = Field(
        None,
        description='Aliases can be set to modify the legend labels. e.g. {{ resourceGroup }}. See docs for more detail.',
    )
    timeGrainUnit: Optional[str] = Field(None, description='@deprecated')
    dimension: Optional[str] = Field(
        None,
        description='@deprecated This property was migrated to dimensionFilters and should only be accessed in the migration',
    )
    dimensionFilter: Optional[str] = Field(
        None,
        description='@deprecated This property was migrated to dimensionFilters and should only be accessed in the migration',
    )
    metricDefinition: Optional[str] = Field(
        None, description='@deprecated Use metricNamespace instead'
    )
    resourceUri: Optional[str] = Field(
        None,
        description='@deprecated Use resourceGroup, resourceName and metricNamespace instead',
    )
    resourceGroup: Optional[str] = Field(
        None, description='@deprecated Use resources instead'
    )
    resourceName: Optional[str] = Field(
        None, description='@deprecated Use resources instead'
    )


class AzureTracesQuery(BaseModel):
    resultFormat: Optional[ResultFormat] = None
    resources: Optional[List[str]] = Field(
        None, description='Array of resource URIs to be queried.'
    )
    operationId: Optional[str] = Field(
        None, description='Operation ID. Used only for Traces queries.'
    )
    traceTypes: Optional[List[str]] = Field(
        None, description='Types of events to filter by.'
    )
    filters: Optional[List[AzureTracesFilter]] = Field(
        None, description='Filters for property values.'
    )
    query: Optional[str] = Field(None, description='KQL query to be executed.')


class GrafanaTemplateVariableQuery(BaseModel):
    __root__: Union[
        AppInsightsMetricNameQuery,
        AppInsightsGroupByQuery,
        SubscriptionsQuery,
        ResourceGroupsQuery,
        ResourceNamesQuery,
        MetricNamespaceQuery,
        MetricDefinitionsQuery,
        MetricNamesQuery,
        WorkspacesQuery,
        UnknownQuery,
    ]


class AzureMonitorQuery(DataQuery):
    subscription: Optional[str] = Field(
        None, description='Azure subscription containing the resource(s) to be queried.'
    )
    subscriptions: Optional[List[str]] = Field(
        None, description='Subscriptions to be queried via Azure Resource Graph.'
    )
    azureMonitor: Optional[AzureMetricQuery] = None
    azureLogAnalytics: Optional[AzureLogsQuery] = None
    azureResourceGraph: Optional[AzureResourceGraphQuery] = None
    azureTraces: Optional[AzureTracesQuery] = None
    grafanaTemplateVariableFn: Optional[GrafanaTemplateVariableQuery] = None
    resourceGroup: Optional[str] = Field(
        None,
        description='Template variables params. These exist for backwards compatiblity with legacy template variables.',
    )
    namespace: Optional[str] = None
    resource: Optional[str] = None
    region: Optional[str] = Field(
        None, description='Azure Monitor query type.\nqueryType: #AzureQueryType'
    )
