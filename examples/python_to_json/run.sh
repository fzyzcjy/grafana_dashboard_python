#!/bin/bash

# use `grafana_dashboard` command directly if you have the package installed
(cd ../.. && python -m grafana_dashboard.grafana_dashboard python-to-json \
  --python-base-dir examples/python_to_json \
  --python-base-package input_python \
  --json-dir examples/python_to_json/output_json
)