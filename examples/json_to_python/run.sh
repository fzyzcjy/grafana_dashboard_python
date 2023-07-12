#!/bin/bash

set -eux

# If you want to test source code instead of published package:
# `python -m grafana_dashboard.grafana_dashboard`
(cd ../.. && grafana_dashboard json-to-python \
  --json-path examples/json_to_python/input.json \
  --python-path examples/json_to_python/output.py
)