from typing import Literal, Dict, List

from grafana_dashboard.model import piechartpanelcfg_types_gen, timeseriespanelcfg_types_gen, tablepanelcfg_types_gen, \
    dashboardlistpanelcfg_types_gen, textpanelcfg_types_gen, logspanelcfg_types_gen, statetimelinepanelcfg_types_gen, \
    heatmappanelcfg_types_gen, statpanelcfg_types_gen
from grafana_dashboard.model.dashboard_types_gen import Panel, ModeEnum, FieldColor, ThresholdsConfig


class TimeSeries(Panel):
    type: Literal['timeseries'] = 'timeseries'
    options: timeseriespanelcfg_types_gen.PanelOptions = timeseriespanelcfg_types_gen.PanelOptions()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.fieldConfig.defaults.custom is None:
            self.fieldConfig.defaults.custom = timeseriespanelcfg_types_gen.GraphFieldConfig()
        if self.fieldConfig.defaults.color is None:
            self.fieldConfig.defaults.color = FieldColor(mode=ModeEnum.palette_classic)


class PieChart(Panel):
    type: Literal['piechart'] = 'piechart'
    options: piechartpanelcfg_types_gen.PanelOptions = piechartpanelcfg_types_gen.PanelOptions()


class Heatmap(Panel):
    type: Literal['heatmap'] = 'heatmap'
    options: heatmappanelcfg_types_gen.PanelOptions = heatmappanelcfg_types_gen.PanelOptions()


class Table(Panel):
    type: Literal['table'] = 'table'
    options: tablepanelcfg_types_gen.PanelOptions = tablepanelcfg_types_gen.PanelOptions()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.fieldConfig.defaults.color is None:
            self.fieldConfig.defaults.color = FieldColor(mode=ModeEnum.thresholds)


class DashboardList(Panel):
    type: Literal['dashlist'] = 'dashlist'
    options: dashboardlistpanelcfg_types_gen.PanelOptions = dashboardlistpanelcfg_types_gen.PanelOptions()


class AlertList(Panel):
    type: Literal['alertlist'] = 'alertlist'


class Text(Panel):
    type: Literal['text'] = 'text'
    options: textpanelcfg_types_gen.PanelOptions = textpanelcfg_types_gen.PanelOptions()


class Logs(Panel):
    type: Literal['logs'] = 'logs'
    options: logspanelcfg_types_gen.PanelOptions = logspanelcfg_types_gen.PanelOptions()


class Stat(Panel):
    type: Literal['stat'] = 'stat'
    options: statpanelcfg_types_gen.PanelOptions = statpanelcfg_types_gen.PanelOptions()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.fieldConfig.defaults.color is None:
            self.fieldConfig.defaults.color = FieldColor(mode=ModeEnum.thresholds)
        if self.fieldConfig.defaults.thresholds is None:
            self.fieldConfig.defaults.thresholds = ThresholdsConfig()


class StateTimeline(Panel):
    type: Literal['state-timeline'] = 'state-timeline'
    options: statetimelinepanelcfg_types_gen.PanelOptions = statetimelinepanelcfg_types_gen.PanelOptions()


# TODO other types

def _dict_nested_fill_default_value(d: Dict, keys: List[str], value):
    if len(keys) == 1:
        if keys[0] not in d:
            d[keys[0]] = value
    else:
        if keys[0] not in d:
            d[keys[0]] = {}
        _dict_nested_fill_default_value(d[keys[0]], keys[1:], value)
