#!/bin/bash

# use `grafana_dashboard` command directly if you have the package installed
(cd ../.. && python -m grafana_dashboard.grafana_dashboard json-to-python \
  --json-path examples/json_to_python/input.json \
  --python-path examples/json_to_python/output.py
)