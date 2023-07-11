import os


def _execute_datamodel_codegen():
    os.system(
        'datamodel-codegen '
        '--input a.yaml '
        '--input-file-type openapi '
        '--output ../grafana_dashboard/models/dashboard_types_gen.py '
        "--custom-file-header '# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND'"
    )


_execute_datamodel_codegen()
