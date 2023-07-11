from typing import Literal

from grafana_dashboard.model import piechartpanelcfg_types_gen, timeseriespanelcfg_types_gen, tablepanelcfg_types_gen
from grafana_dashboard.model.dashboard_types_gen import Panel


class TimeSeries(Panel):
    type: Literal['timeseries'] = 'timeseries'
    options: timeseriespanelcfg_types_gen.PanelOptions = timeseriespanelcfg_types_gen.PanelOptions()


class PieChart(Panel):
    type: Literal['piechart'] = 'piechart'
    options: piechartpanelcfg_types_gen.PanelOptions = piechartpanelcfg_types_gen.PanelOptions()


class Table(Panel):
    type: Literal['table'] = 'table'
    options: tablepanelcfg_types_gen.PanelOptions = tablepanelcfg_types_gen.PanelOptions()
