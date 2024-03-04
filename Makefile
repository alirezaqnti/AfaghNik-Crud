cd .PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrations
migrations:
	poetry run python3 -m core.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python3 -m core.manage migrate

.PHONY: runserver
runserver:
	poetry run python3 -m core.manage runserver

.PHONY: superuser
superuser:
	poetry run python3 -m core.manage createsuperuser

.PHONY: up-dependency-only
up-dependency-only:
	test .env || touch .env
	sudo docker-compose -f docker-compose.dev.yaml up --force-recreate db


.PHONY: update
update: install migrate install-pre-commit;
