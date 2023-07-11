#!/bin/bash

datamodel-codegen \
  --input ../third_party/grok/jsonschema/v10.0.0/kinds/core/dashboard/x/dashboard_types_gen.json \
  --input-file-type openapi \
  --output ../grafana_dashboard/models/dashboard_types_gen/
