from typing import Literal, Dict, List

from grafana_dashboard.model import piechartpanelcfg_types_gen, timeseriespanelcfg_types_gen, tablepanelcfg_types_gen
from grafana_dashboard.model.dashboard_types_gen import Panel


class _DefaultPanel(Panel):
    def __init__(self, **kwargs):
        _dict_nested_fill_default_value(
            kwargs, ['fieldConfig', 'defaults', 'custom'], self.__class__._default_field_config_custom())
        super().__init__(**kwargs)

    @classmethod
    def _default_field_config_custom(cls):
        raise NotImplementedError


class TimeSeries(_DefaultPanel):
    type: Literal['timeseries'] = 'timeseries'
    options: timeseriespanelcfg_types_gen.PanelOptions = timeseriespanelcfg_types_gen.PanelOptions()

    @classmethod
    def _default_field_config_custom(cls):
        return timeseriespanelcfg_types_gen.GraphFieldConfig()


class PieChart(Panel):
    type: Literal['piechart'] = 'piechart'
    options: piechartpanelcfg_types_gen.PanelOptions = piechartpanelcfg_types_gen.PanelOptions()


class Table(Panel):
    type: Literal['table'] = 'table'
    options: tablepanelcfg_types_gen.PanelOptions = tablepanelcfg_types_gen.PanelOptions()


def _dict_nested_fill_default_value(d: Dict, keys: List[str], value):
    if len(keys) == 1:
        if keys[0] not in d:
            d[keys[0]] = value
    else:
        if keys[0] not in d:
            d[keys[0]] = {}
        _dict_nested_fill_default_value(d[keys[0]], keys[1:], value)
