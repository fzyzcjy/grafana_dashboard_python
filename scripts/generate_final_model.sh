#!/bin/bash
set -eux

cp -r ../misc/model_generation/raw_generated/ ../grafana_dashboard/model/
(cd ../grafana_dashboard/model/ && patch < ../../misc/model_generation/manual_patch.patch)
