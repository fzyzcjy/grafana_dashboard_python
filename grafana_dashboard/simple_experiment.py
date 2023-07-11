from grafana_dashboard.generated.dashboard_types_gen import Dashboard

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

sample_dashboard = Dashboard.parse_obj(sample_json)
print(sample_dashboard)
