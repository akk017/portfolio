#!/usr/bin/bash

# Environment Setup
source ./garden_venv/bin/activate
export LAST_COMMIT=$(git --no-pager log main -1 --pretty=%H)

echo $LAST_COMMIT

# Build
mkdocs build

# Deployment
git commitd
mkdocs gh-deploy