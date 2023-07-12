from grafana_dashboard.model.dashboard_types_gen import *
from grafana_dashboard.model.prometheusdataquery_types_gen import *
from grafana_dashboard.model.timeseriespanelcfg_types_gen import *

dashboard = Dashboard(
    title='New dashboard',
    tags=[],
    style=Style.dark,
    timezone='',
    graphTooltip=DashboardCursorSync.not_shared,
    time=Time(from_='now-6h'),
    timepicker=Timepicker(),
    liveNow=False,
    weekStart='',
    schemaVersion=37,
    version=0,
    panels=[
        Panel(
            type='timeseries',
            id=2,
            targets=[
                PrometheusDataQuery(
                    refId='A',
                    datasource={'type': 'prometheus', 'uid': 'PBFA97CFB590B2093'},
                    expr='avg(1 - rate(node_cpu_seconds_total{mode="idle"}[$__rate_interval])) by (instance, job)',
                    range=True,
                    editorMode=QueryEditorMode.code,
                    legendFormat='{{instance}}'
                )
            ],
            title='Panel Title',
            datasource=Datasource(type='prometheus', uid='PBFA97CFB590B2093'),
            gridPos=GridPos(),
            options=PanelOptions(),
            fieldConfig=FieldConfigSource(
                defaults=FieldConfig(
                    thresholds=ThresholdsConfig(
                        mode=ThresholdsMode.absolute,
                        steps=[Threshold(color='green'), Threshold(value=80.0, color='red')]
                    ),
                    color=FieldColor(mode=ModeEnum.palette_classic),
                    custom=GraphFieldConfig(
                        stacking=StackingConfig(mode=StackingMode.none, group='A'),
                        barAlignment=BarAlignment.integer_0,
                        axisPlacement=AxisPlacement.auto,
                        axisColorMode=AxisColorMode.text,
                        axisCenteredZero=False,
                        showPoints=VisibilityMode.auto,
                        lineInterpolation=LineInterpolation.linear,
                        drawStyle=GraphDrawStyle.line,
                        gradientMode=GraphGradientMode.none
                    )
                )
            )
        )
    ],
    annotations=AnnotationContainer(
        list=[
            AnnotationQuery(
                name='Annotations & Alerts',
                datasource=Datasource(type='grafana', uid='-- Grafana --'),
                hide=True,
                iconColor='rgba(0, 211, 255, 1)',
                target=AnnotationTarget(limit=100, matchAny=False, tags=[], type='dashboard'),
                type='dashboard',
                builtIn=1
            )
        ]
    ),
    links=[]
)
