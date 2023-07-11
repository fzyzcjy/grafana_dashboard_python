from pathlib import Path

dir_src = Path(__file__).parents[1] / 'misc/model_generation/raw_generated'
dir_dst = Path(__file__).parents[1] / 'grafana_dashboard/model'

for path_src in dir_src.glob('*.py'):
    path_dst = dir_dst / path_src.name
    # TODO apply patch
    path_dst.write_text(path_src.read_text())
