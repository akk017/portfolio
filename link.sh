#!/usr/bin/env bash

set -e

SRC="/Users/akash-21652/Projects/portfolio/md_compiler/compiler"
DEST="/Users/akash-21652/Projects/portfolio/garden_venv/lib/python3.13/site-packages/compiler"

for item in "$SRC"/*; do
  name=$(basename "$item")
  ln -sf "$item" "$DEST/$name"
done