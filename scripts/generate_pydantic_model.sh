#!/bin/bash

# --input ../third_party/grok/jsonschema/v10.0.0/kinds/core/dashboard/x/dashboard_types_gen.json \
datamodel-codegen \
  --input a.yaml \
  --input-file-type openapi \
  --output ../grafana_dashboard/models/dashboard_types_gen.py
