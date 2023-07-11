from typing import Literal

from grafana_dashboard.model.dashboard_types_gen import Panel


class TimeSeries(Panel):
    type: Literal['timeseries'] = 'timeseries'


class PieChart(Panel):
    type: Literal['piechart'] = 'piechart'


class Table(Panel):
    type: Literal['table'] = 'table'
