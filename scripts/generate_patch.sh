#!/bin/bash

set -eux

diff -Naur ../misc/model_generation/raw_generated/ ../grafana_dashboard/model/ > ../misc/model_generation/manual_patch.patch
