#!/usr/bin/bash

# Enviroment Setup
source ./garden_venv/bin/activate
export LAST_COMMIT=$(git --no-pager log main -1 --pretty=%H)


mkdocs build --clean -d ./test
watchexec -r -w docs -- mkdocs build --dirty -d ./test &
live-server --port=5500 "$(pwd)"/test --watch
