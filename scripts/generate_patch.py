import difflib
from pathlib import Path

dir_before = Path(__file__).parents[1] / 'misc/model_generation/raw_generated'
dir_after = Path(__file__).parents[1] / 'grafana_dashboard/model'
dir_diff = Path(__file__).parents[1] / 'misc/model_generation/manual_patch'

for path_before in dir_before.glob('*.py'):
    path_after = dir_after / path_before.name
    delta = difflib.unified_diff(
        path_before.read_text().split('\n'), path_after.read_text().split('\n'),
        path_before.name, path_after.name,
        lineterm='',
    )
    delta_text = '\n'.join(delta)
    (dir_diff / path_before.name).write_text(delta_text)
