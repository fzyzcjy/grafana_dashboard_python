# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import Field, conint, constr

from grafana_dashboard.model import timeseriespanelcfg_types_gen, piechartpanelcfg_types_gen
from grafana_dashboard.model.lokidataquery_types_gen import LokiDataQuery
from grafana_dashboard.model.prometheusdataquery_types_gen import PrometheusDataQuery
from grafana_dashboard.utils import MyBaseModel


class AnnotationPanelFilter(MyBaseModel):
    exclude: Optional[bool] = Field(
        False, description='Should the specified panels be included or excluded'
    )
    ids: List[conint(ge=0, le=255)] = Field(
        ..., description='Panel IDs that should be included or excluded'
    )


class Datasource(MyBaseModel):
    type: Optional[str] = None
    uid: Optional[str] = None


class AnnotationTarget(MyBaseModel):
    limit: int = Field(
        ...,
        description='Only required/valid for the grafana datasource...\nbut code+tests is already depending on it so hard to change',
    )
    matchAny: bool = Field(
        ...,
        description='Only required/valid for the grafana datasource...\nbut code+tests is already depending on it so hard to change',
    )
    tags: List[str] = Field(
        ...,
        description='Only required/valid for the grafana datasource...\nbut code+tests is already depending on it so hard to change',
    )
    type: str = Field(
        ...,
        description='Only required/valid for the grafana datasource...\nbut code+tests is already depending on it so hard to change',
    )


class DashboardCursorSync(Enum):
    # NOTE RENAMED
    not_shared = 0
    shared_crosshair = 1
    shared_tooltip = 2


class DashboardLinkType(Enum):
    link = 'link'
    dashboards = 'dashboards'


class DataSourceRef(MyBaseModel):
    type: Optional[str] = Field(None, description='The plugin type-id')
    uid: Optional[str] = Field(None, description='Specific datasource instance')


class DynamicConfigValue(MyBaseModel):
    id: Optional[str] = ''
    value: Optional[Any] = None


class ModeEnum(Enum):
    thresholds = 'thresholds'
    palette_classic = 'palette-classic'
    palette_saturated = 'palette-saturated'
    continuous_GrYlRd = 'continuous-GrYlRd'
    fixed = 'fixed'


class FieldColorModeId(Enum):
    thresholds = 'thresholds'
    palette_classic = 'palette-classic'
    palette_saturated = 'palette-saturated'
    continuous_GrYlRd = 'continuous-GrYlRd'
    fixed = 'fixed'


class FieldColorSeriesByMode(Enum):
    min = 'min'
    max = 'max'
    last = 'last'


class Type(Enum):
    graph = 'graph'


class Legend(MyBaseModel):
    show: Optional[bool] = True
    sort: Optional[str] = None
    sortDesc: Optional[bool] = None


class GraphPanel(MyBaseModel):
    type: Type
    legend: Optional[Legend] = Field(
        None, description='@deprecated this is part of deprecated graph panel'
    )


class GridPos(MyBaseModel):
    h: Optional[conint(le=4294967295, gt=0)] = Field(9, description='Panel')
    w: Optional[conint(le=24, gt=0)] = Field(12, description='Panel')
    x: Optional[conint(ge=0, lt=24)] = Field(0, description='Panel x')
    y: Optional[conint(ge=0, le=4294967295)] = Field(0, description='Panel y')
    static: Optional[bool] = Field(None, description='true if fixed')


class Type1(Enum):
    heatmap = 'heatmap'


class HeatmapPanel(MyBaseModel):
    type: Type1


class LibraryPanelRef(MyBaseModel):
    name: str
    uid: str


class LoadingState(Enum):
    NotStarted = 'NotStarted'
    Loading = 'Loading'
    Streaming = 'Streaming'
    Done = 'Done'
    Error = 'Error'


class MappingType(Enum):
    value = 'value'
    range = 'range'
    regex = 'regex'
    special = 'special'


class MatcherConfig(MyBaseModel):
    id: Optional[str] = ''
    options: Optional[Any] = None


class RepeatDirection(Enum):
    h = 'h'
    v = 'v'


class Type2(Enum):
    row = 'row'


class Snapshot(MyBaseModel):
    created: datetime = Field(..., description='TODO docs')
    expires: str = Field(..., description='TODO docs')
    external: bool = Field(..., description='TODO docs')
    externalUrl: str = Field(..., description='TODO docs')
    id: conint(ge=0, le=4294967295) = Field(..., description='TODO docs')
    key: str = Field(..., description='TODO docs')
    name: str = Field(..., description='TODO docs')
    orgId: conint(ge=0, le=4294967295) = Field(..., description='TODO docs')
    updated: datetime = Field(..., description='TODO docs')
    url: Optional[str] = Field(None, description='TODO docs')
    userId: conint(ge=0, le=4294967295) = Field(..., description='TODO docs')


class Match(Enum):
    true = 'true'
    false = 'false'


class SpecialValueMatch(Enum):
    true = 'true'
    false = 'false'
    null = 'null'
    nan = 'nan'
    null_nan = 'null+nan'
    empty = 'empty'


# NOTE REMOVED
# class Target(MyBaseModel):
#     pass


class Threshold(MyBaseModel):
    value: Optional[float] = Field(
        None,
        description='TODO docs\nFIXME the corresponding typescript field is required/non-optional, but nulls currently appear here when serializing -Infinity to JSON',
    )
    color: str = Field(..., description='TODO docs')
    index: Optional[int] = Field(
        None,
        description='Threshold index, an old property that is not needed an should only appear in older dashboards',
    )
    state: Optional[str] = Field(
        None,
        description='TODO docs\nTODO are the values here enumerable into a disjunction?\nSome seem to be listed in typescript comment',
    )


class ThresholdsMode(Enum):
    absolute = 'absolute'
    percentage = 'percentage'


class ValueMappingResult(MyBaseModel):
    text: Optional[str] = None
    color: Optional[str] = None
    icon: Optional[str] = None
    index: Optional[int] = None


class VariableHide(Enum):
    integer_0 = 0
    integer_1 = 1
    integer_2 = 2


class VariableType(Enum):
    query = 'query'
    adhoc = 'adhoc'
    constant = 'constant'
    datasource = 'datasource'
    interval = 'interval'
    textbox = 'textbox'
    custom = 'custom'
    system = 'system'


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


class Style(Enum):
    dark = 'dark'
    light = 'light'


class Time(MyBaseModel):
    from_: Optional[str] = Field('now-6h', alias='from')
    to: Optional[str] = 'now'


class Timepicker(MyBaseModel):
    collapse: Optional[bool] = Field(
        False, description='Whether timepicker is collapsed or not.'
    )
    enable: Optional[bool] = Field(
        True, description='Whether timepicker is enabled or not.'
    )
    hidden: Optional[bool] = Field(
        False, description='Whether timepicker is visible or not.'
    )
    refresh_intervals: Optional[List[str]] = Field(
        ['5s', '10s', '30s', '1m', '5m', '15m', '30m', '1h', '2h', '1d'],
        description='Selectable intervals for auto-refresh.',
    )
    time_options: Optional[List[str]] = Field(
        ['5m', '15m', '1h', '6h', '12h', '24h', '2d', '7d', '30d'],
        description='TODO docs',
    )


class RefreshEnum(Enum):
    bool_False = False


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


class AnnotationQuery(MyBaseModel):
    name: str = Field(..., description='Name of annotation.')
    datasource: Datasource = Field(..., description='TODO: Should be DataSourceRef')
    enable: Optional[bool] = Field(
        True,
        description='When enabled the annotation query is issued with every dashboard refresh',
    )
    hide: Optional[bool] = Field(
        False,
        description='Annotation queries can be toggled on or off at the top of the dashboard.\nWhen hide is true, the toggle is not shown in the dashboard.',
    )
    iconColor: str = Field(
        ..., description='Color to use for the annotation event markers'
    )
    filter: Optional[AnnotationPanelFilter] = None
    target: Optional[AnnotationTarget] = None
    type: Optional[str] = Field(
        None,
        description='TODO -- this should not exist here, it is based on the --grafana-- datasource',
    )


class DashboardLink(MyBaseModel):
    title: str
    type: DashboardLinkType = None  # NOTE MODIFIED
    icon: str = []  # NOTE MODIFIED
    tooltip: str = []  # NOTE MODIFIED
    url: str
    tags: List[str] = []  # NOTE MODIFIED
    asDropdown: Optional[bool] = False
    targetBlank: Optional[bool] = False
    includeVars: Optional[bool] = False
    keepTime: Optional[bool] = False


class DataTransformerConfig(MyBaseModel):
    id: str = Field(..., description='Unique identifier of transformer')
    disabled: Optional[bool] = Field(
        None, description='Disabled transformations are skipped'
    )
    filter: Optional[MatcherConfig] = None
    options: Any = Field(
        ...,
        description='Options to be passed to the transformer\nValid options depend on the transformer id',
    )


class FieldColor(MyBaseModel):
    mode: Union[ModeEnum, Any] = Field(..., description='The main color scheme mode')
    fixedColor: Optional[str] = Field(
        None, description='Stores the fixed color value if mode is fixed'
    )
    seriesBy: Optional[FieldColorSeriesByMode] = None


class Override(MyBaseModel):
    matcher: MatcherConfig
    properties: List[DynamicConfigValue]


class Options(MyBaseModel):
    from_: float = Field(
        ...,
        alias='from',
        description='to and from are `number | null` in current ts, really not sure what to do',
    )
    to: float
    result: ValueMappingResult


class RangeMap(MyBaseModel):
    type: MappingType
    options: Options


class Options1(MyBaseModel):
    pattern: str
    result: ValueMappingResult


class RegexMap(MyBaseModel):
    type: MappingType
    options: Options1


class Options2(MyBaseModel):
    match: Match
    pattern: str
    result: ValueMappingResult


class SpecialValueMap(MyBaseModel):
    type: MappingType
    options: Options2


class ThresholdsConfig(MyBaseModel):
    mode: ThresholdsMode
    steps: List[Threshold] = Field(
        ..., description="Must be sorted by 'value', first value is always -Infinity"
    )


class ValueMap(MyBaseModel):
    type: MappingType
    options: Dict[str, ValueMappingResult]


class ValueMapping(MyBaseModel):
    __root__: Union[ValueMap, RangeMap, RegexMap, SpecialValueMap] = Field(
        ..., description='TODO docs'
    )


class VariableModel(MyBaseModel):
    # NOTE MODIFIED https://github.com/fzyzcjy/yplusplus/issues/10127#issuecomment-1630624655
    id: Optional[str] = None
    type: VariableType
    name: str
    label: Optional[str] = None
    rootStateKey: Optional[str] = None
    global_: Optional[bool] = Field(False, alias='global')
    hide: VariableHide
    skipUrlSync: Optional[bool] = False
    # NOTE MODIFIED https://github.com/fzyzcjy/yplusplus/issues/10127#issuecomment-1630624655
    index: Optional[conint(ge=-2147483648, le=2147483647)] = 0
    state: LoadingState = None  # NOTE MODIFIED
    error: Optional[Dict[str, Any]] = None
    description: Optional[str] = None
    query: Optional[Union[str, Dict[str, Any]]] = Field(
        None, description='TODO: Move this into a separated QueryVariableModel type'
    )
    datasource: Optional[Union[DataSourceRef, str]] = None  # NOTE MODIFIED add `str`

    # NOTE these fields are *not* in schema, but added manually after they are observed
    current: Dict[str, Any] = {}
    includeAll: bool = False
    multi: bool = False
    options: List[Any] = []
    refresh: int = 1
    regex: str = ''
    sort: Optional[int] = None
    tagValuesQuery: Optional[str] = None
    tagQuery: Optional[str] = None
    useTags: Optional[bool] = None
    definition: Optional[str] = None


class Templating(MyBaseModel):
    list: List[VariableModel]  # NOTE MODIFIED


class Status(MyBaseModel):
    operatorStates: Optional[Dict[str, JoinSchemaStatusOperatorState]] = Field(
        None,
        description='operatorStates is a map of operator ID to operator state evaluations.\nAny operator which consumes this kind SHOULD add its state evaluation information to this field.',
    )
    additionalFields: Dict[str, Any] = Field(
        ..., description='additionalFields is reserved for future use'
    )


class AnnotationContainer(MyBaseModel):
    # NOTE MODIFIED - should allow any dict for custom data source
    list: Optional[List[Union[AnnotationQuery, Dict[str, Any]]]] = []  # NOTE MODIFIED


class FieldConfig(MyBaseModel):
    displayName: Optional[str] = Field(
        None,
        description='The display value for this field.  This supports template variables blank is auto',
    )
    displayNameFromDS: Optional[str] = Field(
        None,
        description='This can be used by data sources that return and explicit naming structure for values and labels\nWhen this property is configured, this value is used rather than the default naming strategy.',
    )
    description: Optional[str] = Field(
        None, description='Human readable field metadata'
    )
    path: Optional[str] = Field(
        None,
        description='An explicit path to the field in the datasource.  When the frame meta includes a path,\nThis will default to `${frame.meta.path}/${field.name}\n\nWhen defined, this value can be used as an identifier within the datasource scope, and\nmay be used to update the results',
    )
    writeable: Optional[bool] = Field(
        None,
        description='True if data source can write a value to the path.  Auth/authz are supported separately',
    )
    filterable: Optional[bool] = Field(
        None, description='True if data source field supports ad-hoc filters'
    )
    unit: Optional[str] = Field(None, description='Numeric Options')
    decimals: Optional[float] = Field(
        None, description='Significant digits (for display)'
    )
    min: Optional[float] = None
    max: Optional[float] = None
    mappings: Optional[List[ValueMapping]] = Field(
        [], description='Convert input values into a display string'  # NOTE MODIFIED
    )
    thresholds: Optional[ThresholdsConfig] = None
    color: Optional[FieldColor] = None
    links: Optional[List] = Field(
        None, description='The behavior when clicking on a result'
    )
    noValue: Optional[str] = Field(None, description='Alternative to empty string')
    # NOTE MODIFIED
    # TODO add other panel options...
    custom: Optional[Union[
        timeseriespanelcfg_types_gen.GraphFieldConfig,
        Dict[str, Any]
    ]] = Field(
        None,
        description='custom is specified by the PanelFieldConfig field\nin panel plugin schemas.',
    )


class FieldConfigSource(MyBaseModel):
    defaults: FieldConfig = FieldConfig()  # NOTE MODIFIED
    overrides: List[Override] = []  # NOTE MODIFIED


class Panel(MyBaseModel):
    type: constr(min_length=1) = Field(
        ..., description='The panel plugin type id. May not be empty.'
    )
    id: Optional[conint(ge=0, le=4294967295)] = Field(None, description='TODO docs')
    pluginVersion: Optional[str] = Field(
        None,
        description='FIXME this almost certainly has to be changed in favor of scuemata versions',
    )
    tags: Optional[List[str]] = Field(None, description='TODO docs')
    # NOTE MODIFIED, originally it is (empty class) `Target`
    targets: Optional[List[Union[
        PrometheusDataQuery,
        LokiDataQuery,
        Dict[str, Any]
    ]]] = Field(None)
    title: Optional[str] = Field(None, description='Panel title.')
    description: Optional[str] = Field(None, description='Description.')
    transparent: Optional[bool] = Field(
        False, description='Whether to display the panel without a background.'
    )
    datasource: Optional[Union[str, Datasource]] = Field(  # NOTE MODIFIED add `str`
        None, description='The datasource used in all targets.'
    )
    gridPos: Optional[GridPos] = None
    links: Optional[List[DashboardLink]] = Field(
        None,
        description='Panel links.\nTODO fill this out - seems there are a couple variants?',
    )
    repeat: Optional[str] = Field(
        None, description='Name of template variable to repeat for.'
    )
    repeatDirection: Optional[RepeatDirection] = Field(
        'h',
        description='Direction to repeat in if \'repeat\' is set.\n"h" for horizontal, "v" for vertical.\nTODO this is probably optional',
    )
    repeatPanelId: Optional[int] = Field(None, description='Id of the repeating panel.')
    maxDataPoints: Optional[float] = Field(None, description='TODO docs')
    thresholds: Optional[Any] = Field(  # NOTE MODIFIED List->Any, since see double in production
        None,
        description='TODO docs - seems to be an old field from old dashboard alerts?',
    )
    timeRegions: Optional[List] = Field(None, description='TODO docs')
    transformations: List[DataTransformerConfig] = []  # NOTE MODIFIED
    interval: Optional[str] = Field(
        None, description='TODO docs\nTODO tighter constraint'
    )
    timeFrom: Optional[str] = Field(
        None, description='TODO docs\nTODO tighter constraint'
    )
    timeShift: Optional[str] = Field(
        None, description='TODO docs\nTODO tighter constraint'
    )
    libraryPanel: Optional[LibraryPanelRef] = None
    # NOTE MODIFIED
    # TODO add other panel options...
    options: Union[
        timeseriespanelcfg_types_gen.PanelOptions,
        piechartpanelcfg_types_gen.PanelOptions,
        Dict[str, Any]
    ] = Field(
        ...,
        description='options is specified by the PanelOptions field in panel\nplugin schemas.',
    )
    fieldConfig: FieldConfigSource = FieldConfigSource()  # NOTE MODIFIED


class RowPanel(MyBaseModel):
    type: Type2 = 'row'  # NOTE MODIFIED
    collapsed: Optional[bool] = False
    title: Optional[str] = None
    datasource: Optional[Union[Datasource, str]] = Field(  # NOTE MODIFIED add `str`
        None, description='Name of default datasource.'
    )
    gridPos: Optional[GridPos] = None
    id: Optional[conint(ge=0, le=4294967295)] = None  # NOTE MODIFIED
    panels: List[Union[Panel, GraphPanel, HeatmapPanel]] = []  # NOTE MODIFIED
    repeat: Optional[str] = Field(
        None, description='Name of template variable to repeat for.'
    )


# NOTE MODIFIED rename "Spec" -> "Dashboard" to avoid confusion
class Dashboard(MyBaseModel):
    id: Optional[int] = Field(
        None,
        description='Unique numeric identifier for the dashboard.\nTODO must isolate or remove identifiers local to a Grafana instance...?',
    )
    uid: Optional[str] = Field(
        None,
        description='Unique dashboard identifier that can be generated by anyone. string (8-40)',
    )
    title: Optional[str] = Field(None, description='Title of dashboard.')
    description: Optional[str] = Field(None, description='Description of dashboard.')
    revision: Optional[int] = Field(
        None,
        description='This property should only be used in dashboards defined by plugins.  It is a quick check\nto see if the version has changed since the last time.  Unclear why using the version property\nis insufficient.',
    )
    gnetId: Optional[str] = Field(
        None,
        description='For dashboards imported from the https://grafana.com/grafana/dashboards/ portal',
    )
    tags: Optional[List[str]] = Field(
        None, description='Tags associated with dashboard.'
    )
    style: Optional[Style] = Field('dark', description='Theme of dashboard.')
    timezone: Optional[str] = Field(
        'browser',
        description='Timezone of dashboard. Accepts IANA TZDB zone ID or "browser" or "utc".',
    )
    editable: Optional[bool] = Field(
        True, description='Whether a dashboard is editable or not.'
    )
    graphTooltip: DashboardCursorSync
    time: Optional[Time] = Field(
        None,
        description='Time range for dashboard, e.g. last 6 hours, last 7 days, etc',
    )
    timepicker: Optional[Timepicker] = Field(
        None,
        description='TODO docs\nTODO this appears to be spread all over in the frontend. Concepts will likely need tidying in tandem with schema changes',
    )
    fiscalYearStartMonth: Optional[conint(ge=0, lt=12)] = Field(
        0,
        description='The month that the fiscal year starts on.  0 = January, 11 = December',
    )
    liveNow: Optional[bool] = Field(
        None,
        description='When set to true, the dashboard will redraw panels at an interval matching the pixel width.\nThis will keep data "moving left" regardless of the query refresh rate.  This setting helps\navoid dashboards presenting stale live data',
    )
    weekStart: Optional[str] = Field(None, description='TODO docs')
    refresh: Optional[Union[RefreshEnum, str]] = Field(
        None,
        description='Refresh rate of dashboard. Represented via interval string, e.g. "5s", "1m", "1h", "1d".',
    )
    schemaVersion: Optional[conint(ge=0, le=65535)] = Field(
        36,
        description="Version of the JSON schema, incremented each time a Grafana update brings\nchanges to said schema.\nTODO this is the existing schema numbering system. It will be replaced by Thema's themaVersion",
    )
    version: Optional[conint(ge=0, le=4294967295)] = Field(
        None,
        description='Version of the dashboard, incremented each time the dashboard is updated.',
    )
    panels: Optional[List[Union[Panel, RowPanel, GraphPanel, HeatmapPanel]]] = None
    templating: Templating = Field(Templating(list=[]), description='TODO docs')  # NOTE MODIFIED
    annotations: Optional[AnnotationContainer] = AnnotationContainer()  # NOTE MODIFIED
    links: Optional[List[DashboardLink]] = Field(None, description='TODO docs')
    snapshot: Optional[Snapshot] = None

    # NOTE MODIFIED add
    def auto_panel_ids(self):
        from grafana_dashboard.utils import dashboard_auto_panel_ids
        dashboard_auto_panel_ids(self)
        return self

    # NOTE MODIFIED add
    def to_grafana_json(self):
        return self.json(
            # NOTE need by_alias for `Time.from_` #10119
            by_alias=True,
            sort_keys=True,
            indent=2,
        )

# NOTE MODIFIED rm this "Dashboard" to avoid confusion
# class Dashboard(MyBaseModel):
