
SHELL := /bin/bash

.ONESHELL:
.PHONY: build webui run-server clean dev

PROJECT_HOME=/Users/akash-21652/Projects/portfolio
GARDEN_ENV=$(PROJECT_HOME)/garden_venv/bin/activate

BUILD=build
MD_COMPILER=md_compiler
TEMPLATES=templates
WEBUI_NAME=imagedb
IMAGEDB_API=imagedb-api
NAV=nav

webui:
	source $$HOME/.nvm/nvm.sh && nvm use 24
	cd "$(PROJECT_HOME)/$(WEBUI_NAME)"
	set -a && source .env && set +a
	nvm use
	npm run dev

run-server:
	cd "$(PROJECT_HOME)/$(WEBUI_NAME)" 
	shapeshifter
	
build-nav: clean-nav
	source $$HOME/.nvm/nvm.sh && nvm use 24
	cd "$(PROJECT_HOME)/$(NAV)"
	npm run build
	mv ./dist/assets/index.js "$(PROJECT_HOME)/$(TEMPLATES)/$(NAV)"
	mv ./dist/assets/index.css "$(PROJECT_HOME)/$(TEMPLATES)/$(NAV)"

build: clean build-nav
	source $(GARDEN_ENV)
	cd "$(PROJECT_HOME)/$(MD_COMPILER)"
	pip3 install .
	cd ..
	$(MAKE) clean
	cd "$(PROJECT_HOME)"
	python3 -m compiler

clean:
	cd "$(PROJECT_HOME)/$(MD_COMPILER)"
	rm -rf build md_compiler.egg-info
	
clean-nav:
	cd "$(PROJECT_HOME)/$(NAV)"
	rm -rf dist

serve: build
	source $(GARDEN_ENV)
	cd "$(PROJECT_HOME)"
	python3 -m compiler --watch

deploy: build
	firebase deploy

watch:
	cd "$(PROJECT_HOME)/$(BUILD)"
	live-server --host=0.0.0.0 --port=5500 "$(pwd)" --watch --no-browser

dev:
	trap 'kill 0' SIGINT
	$(MAKE) serve &
	$(MAKE) watch &
	wait
