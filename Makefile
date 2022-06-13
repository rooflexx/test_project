SRCPATH := $(CURDIR)
SHELL := /bin/bash
PROJECTNAME := $(shell basename $(CURDIR))


define HELP

Manage $(PROJECTNAME). Usage:

setup                   - Setup project for local development
lint                    - Lint the code with black
migrate                - Make migrations && Migrate
format                  - Format the code with black, autoflake, isort
start               	- Start the services
stop		    	- Stop the services using docker-compose
stop-v          	- Stop all the services and remove the volumes
logs            	- See the logs of services - Listen for events

endef

export HELP



stop:
	docker-compose down

stop-v:
	docker-compose down -v

start:
	docker-compose up -d --build

logs:
	docker-compose logs -f

lint:
	 bash ./scripts/lint.sh

format:
	bash ./scripts/format.sh

setup:
		@python3 -m venv $(ENV)
		@echo -n 'Installing dependencies... '
		@$(ENV)/bin/python -m pip install -r requirements/local.txt
		@echo 'Done installing dependencies..'
		@echo 'Activate your virtual environment with: (source $(ENV)/bin/activate)'

all help:
	@echo "$$HELP"

