#!/bin/bash

set -eux

# If you want to test source code instead of published package:
# `python -m grafana_dashboard.grafana_dashboard`
(cd ../.. && grafana_dashboard python-to-json \
  --python-base-dir examples/python_to_json \
  --python-base-package input_python \
  --json-dir examples/python_to_json/output_json
)