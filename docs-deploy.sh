#!/usr/bin/bash

# Environment Setup
source ./garden_venv/bin/activate
export PORTFOLIO_LAST_COMMIT=$(git --no-pager log main -1 --pretty=%H)

# Build
mkdocs build

# Deployment
git commitd
mkdocs gh-deploy