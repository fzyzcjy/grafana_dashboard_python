import importlib
import sys
from pathlib import Path


def convert(
        python_dir: Path,
        python_package: str,
        json_dir: Path,
):
    assert python_dir.is_dir()
    assert json_dir.is_dir()

    sys.path.append(str(python_dir))

    mod = importlib.import_module(python_package)

    TODO


def _python_package_to_dir(s: str) -> str:
    return s.replace('.', '/')


def _python_dir_to_package(s: str) -> str:
    return s.replace('/', '.')
