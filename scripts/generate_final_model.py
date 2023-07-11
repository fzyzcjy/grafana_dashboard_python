import os
from pathlib import Path

dir_src = Path(__file__).parents[1] / 'misc/model_generation/raw_generated'
dir_dst = Path(__file__).parents[1] / 'grafana_dashboard/model'

path_patch = Path(__file__).parents[1] / 'misc/model_generation/manual_patch.patch'

for path_src in dir_src.glob('*.py'):
    path_dst = dir_dst / path_src.name
    path_dst.write_text(path_src.read_text())

cmd = f'cd {dir_dst} && patch < {path_patch}'
print(f'Execute: {cmd}')
ret = os.system(cmd)
assert ret == 0
