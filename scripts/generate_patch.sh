#!/bin/bash

set -eux

diff -Nau ../misc/model_generation/raw_generated/ ../grafana_dashboard/model/ > ../misc/model_generation/manual_patch.patch
