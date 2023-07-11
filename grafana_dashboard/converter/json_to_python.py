import json
from io import StringIO
from pathlib import Path

import rich

from grafana_dashboard.model.dashboard_types_gen import Spec


def convert(
        json_path: Path,
        python_path: Path,
):
    json_dict = json.loads(json_path.read_text())
    dashboard = Spec.parse_obj(json_dict)

    buf = StringIO()
    rich.console.Console(file=buf).print(dashboard, overflow='ignore', width=100000000, crop=False)
    python_code = buf.getvalue()

    python_path.write_text(python_code)
