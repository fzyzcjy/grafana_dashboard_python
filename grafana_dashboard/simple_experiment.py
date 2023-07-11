from grafana_dashboard.generated.dashboard_types_gen import *

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
print(repr(sample_dashboard))

copied_repr_of_sample_dashboard = Spec(id=None, uid=None, title='New dashboard', description=None, revision=None,
                                       gnetId=None, tags=[], style=Style.dark, timezone='', editable=True,
                                       graphTooltip=DashboardCursorSync.integer_0,
                                       # NOTE HACK `Time`
                                       time=Time.parse_obj({'from': 'now-6h', 'to': 'now'}),
                                       timepicker=None, fiscalYearStartMonth=0, liveNow=False, weekStart='',
                                       refresh=None, schemaVersion=37, version=0, panels=[
        Panel(type='timeseries', id=2, pluginVersion=None, tags=None, targets=[Target()], title='Panel Title',
              description=None, transparent=False, datasource=Datasource(type='prometheus', uid='PBFA97CFB590B2093'),
              gridPos=GridPos(h=9, w=12, x=0, y=0, static=None), links=None, repeat=None,
              repeatDirection=RepeatDirection.h, repeatPanelId=None, maxDataPoints=None, thresholds=None,
              timeRegions=None, transformations=[], interval=None, timeFrom=None, timeShift=None, libraryPanel=None,
              options={'legend': {'calcs': [], 'displayMode': 'list', 'placement': 'bottom', 'showLegend': True},
                       'tooltip': {'mode': 'single', 'sort': 'none'}}, fieldConfig=FieldConfigSource(
                defaults=FieldConfig(displayName=None, displayNameFromDS=None, description=None, path=None,
                                     writeable=None, filterable=None, unit=None, decimals=None, min=None, max=None,
                                     mappings=[], thresholds=ThresholdsConfig(mode=ThresholdsMode.absolute, steps=[
                        Threshold(value=None, color='green', index=None, state=None),
                        Threshold(value=80.0, color='red', index=None, state=None)]),
                                     color=FieldColor(mode=ModeEnum.palette_classic, fixedColor=None, seriesBy=None),
                                     links=None, noValue=None,
                                     custom={'axisCenteredZero': False, 'axisColorMode': 'text', 'axisLabel': '',
                                             'axisPlacement': 'auto', 'barAlignment': 0, 'drawStyle': 'line',
                                             'fillOpacity': 0, 'gradientMode': 'none',
                                             'hideFrom': {'legend': False, 'tooltip': False, 'viz': False},
                                             'lineInterpolation': 'linear', 'lineWidth': 1, 'pointSize': 5,
                                             'scaleDistribution': {'type': 'linear'}, 'showPoints': 'auto',
                                             'spanNulls': False, 'stacking': {'group': 'A', 'mode': 'none'},
                                             'thresholdsStyle': {'mode': 'off'}}), overrides=[]))],
                                       templating=Templating(list=[]), annotations=AnnotationContainer(list=[
        AnnotationQuery(name='Annotations & Alerts', datasource=Datasource(type='grafana', uid='-- Grafana --'),
                        enable=True, hide=True, iconColor='rgba(0, 211, 255, 1)', filter=None,
                        target=AnnotationTarget(limit=100, matchAny=False, tags=[], type='dashboard'),
                        type='dashboard')]), links=[], snapshot=None)

print(sample_dashboard == copied_repr_of_sample_dashboard)
