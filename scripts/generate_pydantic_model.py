import os
from pathlib import Path


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


dir_src = Path(__file__).parents[1] / 'third_party/grok/jsonschema/v10.0.0/kinds'
dir_target = Path(__file__).parents[1] / 'grafana_dashboard/generated'

_ensure_python_package(dir_target)

for p_src in dir_src.glob('**/*.json'):
    p_target = dir_target / f'{p_src.stem}.py'
    print(f'Handle: {p_src} -> {p_target}')

    _execute_datamodel_codegen(
        path_input=p_src,
        path_output=p_target,
    )
