import os
from pathlib import Path


def _execute_datamodel_codegen():
    os.system(
        'datamodel-codegen '
        '--input a.yaml '
        '--input-file-type openapi '
        '--output ../grafana_dashboard/models/dashboard_types_gen.py '
        "--custom-file-header '# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND'"
    )


def _ensure_python_package(d: Path):
    d.mkdir(exist_ok=True)
    (d / '__init__.py').write_text('')


dir_src = Path(__file__).parents[1] / 'third_party/grok/jsonschema/v10.0.0/kinds'
dir_target = Path(__file__).parents[1] / 'grafana_dashboard/generated'

_ensure_python_package(dir_target)

_execute_datamodel_codegen()
