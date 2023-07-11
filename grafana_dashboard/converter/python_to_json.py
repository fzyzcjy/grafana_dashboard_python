import importlib
import sys
from pathlib import Path

from grafana_dashboard.model.dashboard_types_gen import Spec


def convert_package(
        python_base_dir: Path,
        python_package: str,
        json_dir: Path,
):
    assert python_base_dir.is_dir()
    assert json_dir.is_dir()

    sys.path.append(str(python_base_dir))

    python_package_dir = python_base_dir / _python_package_to_dir(python_package)
    for path_python in python_package_dir.glob('**/*.py'):
        if path_python.name in ('__init__.py', '__main__.py'):
            continue
        mod = importlib.import_module(python_package)
        dashboard = mod.dashboard
        assert isinstance(dashboard, Spec)

        path_json = json_dir / path_python.parent.relative_to(python_package_dir) / f'{path_python.stem}.json'
        convert_single(dashboard=dashboard, json_path=path_json)


def convert_single(dashboard: Spec, json_path: Path):
    json_path.write_text(dashboard.to_grafana_json())


def _python_package_to_dir(s: str) -> str:
    return s.replace('.', '/')


def _python_dir_to_package(s: str) -> str:
    return s.replace('/', '.')
