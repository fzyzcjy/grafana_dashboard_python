import importlib
import sys
from pathlib import Path

import typer

from grafana_dashboard.model.dashboard_types_gen import Spec


def convert_package(
        python_base_dir: Path = typer.Option(...),
        python_base_package: str = typer.Option(...),
        json_dir: Path = typer.Option(...),
):
    assert python_base_dir.is_dir()
    assert json_dir.is_dir()

    sys.path.append(str(python_base_dir))

    python_package_dir = python_base_dir / _python_package_to_dir(python_base_package)
    assert python_package_dir.is_dir(), f'{python_package_dir} should be a directory'

    for path_python in python_package_dir.glob('**/*.py'):
        python_package_name = _python_dir_to_package(path_python, python_base_dir)
        print(f'convert_package examine {path_python} ({python_package_name})')

        if path_python.name in ('__init__.py', '__main__.py'):
            continue
        mod = importlib.import_module(python_package_name)
        dashboard = mod.dashboard
        assert isinstance(dashboard, Spec)

        path_json = json_dir / str(path_python.parent.relative_to(python_package_dir)).replace('_', '-') \
                    / f'{path_python.stem.replace("_", "-")}.json'

        print(f'convert_package generate {path_python} -> {path_json}')
        convert_single(dashboard=dashboard, json_path=path_json)


def convert_single(dashboard: Spec, json_path: Path):
    json_path.write_text(dashboard.to_grafana_json())


def _python_package_to_dir(s: str) -> str:
    return s.replace('.', '/')


def _python_dir_to_package(path_python: Path, python_base_dir: Path) -> str:
    return str(path_python.relative_to(python_base_dir)).replace('/', '.').removesuffix('.py')
