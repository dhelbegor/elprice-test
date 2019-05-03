ARGS = $(filter-out $@,$(MAKECMDGOALS))
MAKEFLAGS += --silent
.DEFAULT_GOAL := help

PROJECTNAME = elprice

DOCKER_EXEC = docker exec -it $(PROJECTNAME)_
DOCKER_IEXEC = docker exec -i $(PROJECTNAME)_
MANAGE = $(DOCKER_EXEC)web ./manage.py

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

status: ## Show status services
	docker-compose ps

up: ## Init services
	docker-compose up -d
start: up ## Alias from "up"

up_log: ## Init services (with logs)
	docker-compose up

down: ## Pause services
	docker-compose stop
	
stop: down ## Alias from "down"

bash: ## Open a bash in the specific service
	docker exec -it $(PROJECTNAME)_$(ARGS) bash

cmd: ## Execut a specific command in a container
	$(DOCKER_EXEC)$(ARGS)

manage: ## Execute a django manage command. Ex.: make manage "makemigrations newsletter zero"
	$(MANAGE) $(ARGS)

runserver: ## Init the runserver
	echo ~~ Starting server at: http://localhost:8000/
	$(MANAGE) runserver 0:8000
run: up && runserver ## Alias of "runserver" an "up"

migrate: ## Appply migrations for all apps
	$(MANAGE) migrate

mmigrate: ## Create & apply migrations
	$(MANAGE) makemigrations
	$(MANAGE) migrate

rebuild: ## Rebuild all docker services
	docker-compose kill
	docker-compose build

update: ## Update requirements and apply migrations: requirements.txt > apply migrations
	$(DOCKER_EXEC)web pip install -r requirements.txt -q
	$(MANAGE) migrate

notebook: ## Init Jupyter Notebook shell ( if installed )
	$(MANAGE) "shell_plus --notebook"


db-backup: ## Create a database backup "db_backup.sql"
	$(DOCKER_EXEC)db pg_dump $(PROJECTNAME) -U $(PROJECTNAME) > schema/schema.sql

db-restore: ## Restore the database "schema.sql"
	docker cp schema/schema.sql $(PROJECTNAME)_db:/tmp/db.sql
	$(DOCKER_EXEC)db dropdb $(PROJECTNAME) -U $(PROJECTNAME)
	$(DOCKER_EXEC)db createdb $(PROJECTNAME) -U $(PROJECTNAME)
	$(DOCKER_EXEC)db "psql $(PROJECTNAME) -U $(PROJECTNAME) < /tmp/db.sql"
	#$(DOCKER_EXEC)db rm /tmp/db.sql

db-reset: ## Clean  the database
	$(DOCKER_EXEC)db dropdb $(PROJECTNAME) -U $(PROJECTNAME)
	$(DOCKER_EXEC)db createdb $(PROJECTNAME) -U $(PROJECTNAME)
	$(MANAGE) migrate

dump: ## Dump data
	$(MANAGE) dumpdata products --format=json --indent 2 > fixtures/products.json

load: ## Load data
	$(MANAGE) loaddata fixtures/products.json

own: ## Muda o ownership de todos os arquivos do diretório para o usuário atual
	sudo chown $$(id -u):$$(id -g) -R .

%:
	@:
