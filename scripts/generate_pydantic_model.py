import json
import os
from pathlib import Path
from typing import Dict


def _execute_datamodel_codegen(
        path_input: Path,
        path_output: Path,
):
    os.system(
        'datamodel-codegen '
        f'--input {path_input} '
        '--input-file-type openapi '
        f'--output {path_output} '
        "--custom-file-header '# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND'"
    )


def _ensure_python_package(d: Path):
    d.mkdir(parents=True, exist_ok=True)
    (d / '__init__.py').write_text('')


def _transform_openapi_schema(raw: Dict) -> Dict:
    return TODO


dir_src = Path(__file__).parents[1] / 'third_party/grok/jsonschema/v10.0.0/kinds'
dir_target = Path(__file__).parents[1] / 'grafana_dashboard/generated'

_ensure_python_package(dir_target)

p_temp = Path('/tmp/generate_pydantic_model_temp.json')

for p_src in dir_src.glob('**/*.json'):
    # TODO temp
    if p_src.name != 'dashboard_types_gen.json':
        continue

    p_target = dir_target / f'{p_src.stem}.py'
    print(f'Handle: {p_src} -> {p_target}')

    p_temp.write_text(json.dumps(_transform_openapi_schema(json.loads(p_src.read_text()))))

    _execute_datamodel_codegen(
        path_input=p_temp,
        path_output=p_target,
    )
