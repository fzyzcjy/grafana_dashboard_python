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


def _dict_rename_key(d: Dict, key_old: str, key_new: str):
    assert key_new != key_old
    d[key_new] = d[key_old]
    del d[key_old]


def _sanitize_schema_key(raw_key: str) -> str:
    return raw_key.replace('.', '_').replace('#', '')


def _transform_openapi_schema(raw_str: str) -> str:
    primary_dict = json.loads(raw_str)
    schemas = primary_dict['components']['schemas']

    interest_schema_keys = [
        schema_key for schema_key in schemas
        if _sanitize_schema_key(schema_key) != schema_key
    ]

    for schema_key in interest_schema_keys:
        _dict_rename_key(schemas, schema_key, _sanitize_schema_key(schema_key))

    transformed_str = json.dumps(primary_dict)

    for schema_key in interest_schema_keys:
        prefix = '#/components/schemas/'
        transformed_str = transformed_str.replace(prefix + schema_key, prefix + _sanitize_schema_key(schema_key))

    return transformed_str


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

    p_temp.write_text(_transform_openapi_schema(p_src.read_text()))

    _execute_datamodel_codegen(
        path_input=p_temp,
        path_output=p_target,
    )
