import json
from io import StringIO

import rich.console

from grafana_dashboard.model.dashboard_types_gen import *
from grafana_dashboard.model.prometheusdataquery_types_gen import *
from grafana_dashboard.model.timeseriespanelcfg_types_gen import *

# experiment, just create one from GUI and copy it here
sample_json = {
    "annotations": {
        "list": [
            {
                "builtIn": 1,
                "datasource": {
                    "type": "grafana",
                    "uid": "-- Grafana --"
                },
                "enable": True,
                "hide": True,
                "iconColor": "rgba(0, 211, 255, 1)",
                "name": "Annotations & Alerts",
                "target": {
                    "limit": 100,
                    "matchAny": False,
                    "tags": [],
                    "type": "dashboard"
                },
                "type": "dashboard"
            }
        ]
    },
    "editable": True,
    "fiscalYearStartMonth": 0,
    "graphTooltip": 0,
    "links": [],
    "liveNow": False,
    "panels": [
        {
            # NOTE HACK START (maybe b/c grafana 10 add fields?
            "transformations": [],
            # NOTE HACK END
            "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
            },
            "fieldConfig": {
                "defaults": {
                    "color": {
                        "mode": "palette-classic"
                    },
                    "custom": {
                        "axisCenteredZero": False,
                        "axisColorMode": "text",
                        "axisLabel": "",
                        "axisPlacement": "auto",
                        "barAlignment": 0,
                        "drawStyle": "line",
                        "fillOpacity": 0,
                        "gradientMode": "none",
                        "hideFrom": {
                            "legend": False,
                            "tooltip": False,
                            "viz": False
                        },
                        "lineInterpolation": "linear",
                        "lineWidth": 1,
                        "pointSize": 5,
                        "scaleDistribution": {
                            "type": "linear"
                        },
                        "showPoints": "auto",
                        "spanNulls": False,
                        "stacking": {
                            "group": "A",
                            "mode": "none"
                        },
                        "thresholdsStyle": {
                            "mode": "off"
                        }
                    },
                    "mappings": [],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {
                                "color": "green",
                                "value": None
                            },
                            {
                                "color": "red",
                                "value": 80
                            }
                        ]
                    }
                },
                "overrides": []
            },
            "gridPos": {
                "h": 9,
                "w": 12,
                "x": 0,
                "y": 0
            },
            "id": 2,
            "options": {
                "legend": {
                    "calcs": [],
                    "displayMode": "list",
                    "placement": "bottom",
                    "showLegend": True
                },
                "tooltip": {
                    "mode": "single",
                    "sort": "none"
                }
            },
            "targets": [
                {
                    "datasource": {
                        "type": "prometheus",
                        "uid": "PBFA97CFB590B2093"
                    },
                    "editorMode": "code",
                    "expr": "avg(1 - rate(node_cpu_seconds_total{mode=\"idle\"}[$__rate_interval])) by (instance, job)",
                    "legendFormat": "__auto",
                    "range": True,
                    "refId": "A"
                }
            ],
            "title": "Panel Title",
            "type": "timeseries"
        }
    ],
    "schemaVersion": 37,
    "style": "dark",
    "tags": [],
    "templating": {
        "list": []
    },
    "time": {
        "from": "now-6h",
        "to": "now"
    },
    "timepicker": {},
    "timezone": "",
    "title": "New dashboard",
    "version": 0,
    "weekStart": ""
}

sample_dashboard = Spec.parse_obj(sample_json)
print(sample_dashboard)
print('sample_dashboard', repr(sample_dashboard))

# HACK REGEX
# <(\w+\.\w+): .+>
# $1

copied_repr_of_sample_dashboard = Spec(
    title='New dashboard',
    tags=[],
    style=Style.dark,
    timezone='',
    graphTooltip=DashboardCursorSync.integer_0,
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
                    datasource={
                        'type': 'prometheus',
                        'uid': 'PBFA97CFB590B2093'
                    },
                    expr='avg(1 - rate(node_cpu_seconds_total{mode="idle"}[$__rate_interval])) by (instance, job)',
                    range=True,
                    editorMode=QueryEditorMode.code,
                    legendFormat='__auto'
                )
            ],
            title='Panel Title',
            datasource=Datasource(type='prometheus', uid='PBFA97CFB590B2093'),
            gridPos=GridPos(),
            transformations=[],
            options=PanelOptions(
                legend=VizLegendOptions(
                    displayMode=LegendDisplayMode.list,
                    placement=LegendPlacement.bottom,
                    showLegend=True,
                    calcs=[]
                ),
                tooltip=VizTooltipOptions(
                    mode=TooltipDisplayMode.single,
                    sort=SortOrder.none
                )
            ),
            fieldConfig=FieldConfigSource(
                defaults=FieldConfig(
                    mappings=[],
                    thresholds=ThresholdsConfig(
                        mode=ThresholdsMode.absolute,
                        steps=[
                            Threshold(color='green'),
                            Threshold(value=80.0, color='red')
                        ]
                    ),
                    color=FieldColor(mode=ModeEnum.palette_classic),
                    custom=GraphFieldConfig(
                        hideFrom=HideSeriesConfig(
                            tooltip=False,
                            legend=False,
                            viz=False
                        ),
                        stacking=StackingConfig(
                            mode=StackingMode.none,
                            group='A'
                        ),
                        barAlignment=BarAlignment.integer_0,
                        axisPlacement=AxisPlacement.auto,
                        axisColorMode=AxisColorMode.text,
                        axisLabel='',
                        scaleDistribution=ScaleDistributionConfig(
                            type=ScaleDistribution.linear
                        ),
                        axisCenteredZero=False,
                        showPoints=VisibilityMode.auto,
                        pointSize=5.0,
                        fillOpacity=0.0,
                        lineWidth=1.0,
                        lineInterpolation=LineInterpolation.linear,
                        spanNulls=False,
                        drawStyle=GraphDrawStyle.line,
                        gradientMode=GraphGradientMode.none,
                        thresholdsStyle=GraphThresholdsStyleConfig(
                            mode=GraphTresholdsStyleMode.off
                        )
                    )
                ),
                overrides=[]
            )
        )
    ],
    templating=Templating(list=[]),
    annotations=AnnotationContainer(
        list=[
            AnnotationQuery(
                name='Annotations & Alerts',
                datasource=Datasource(type='grafana', uid='-- Grafana --'),
                hide=True,
                iconColor='rgba(0, 211, 255, 1)',
                target=AnnotationTarget(
                    limit=100,
                    matchAny=False,
                    tags=[],
                    type='dashboard'
                ),
                type='dashboard'
            )
        ]
    ),
    links=[]
)
print('copied_repr_of_sample_dashboard', repr(copied_repr_of_sample_dashboard))

# https://github.com/fzyzcjy/yplusplus/issues/10116#issuecomment-1630070853
# assert sample_dashboard == copied_repr_of_sample_dashboard

# NOTE need by_alias for `Time.from_` #10119
sample_dashboard_json = json.loads(sample_dashboard.json(by_alias=True))

print('sample_json', json.dumps(sample_json))
print('sample_dashboard.json', json.dumps(sample_dashboard_json))
# assert sample_json == sample_dashboard_json
# # %%

buf = StringIO()
rich.console.Console(file=buf).print(sample_dashboard, overflow='ignore', width=100000000, crop=False)
s = buf.getvalue()
print(s)
