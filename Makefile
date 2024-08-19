.PHONY: help pull-$(CONFIG_DIR) push-$(CONFIG_DIR) makemigrations migrate runserver superuser collectstatic test install-nginx uninstall-nginx install-gunicorn uninstall-gunicorn

# Makefile

help:			## Show this help.
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

makemigrations: ## Make migrations
	poetry run python manage.py makemigrations

migrate: makemigrations ## Apply migrations
	poetry run python manage.py migrate

runserver: migrate ## Run the Django development server
	poetry run python manage.py runserver

superuser: ## Create a superuser
	poetry run python manage.py createsuperuser --no-input

collectstatic: ## Collect static files
	poetry run python manage.py collectstatic --noinput

test: ## Run tests
	poetry run python manage.py test

DJANGO_ENVIRONMENT ?= development
CONFIG_DIR := deploy/$(DJANGO_ENVIRONMENT)

pull-deploy: 	## Pull Nginx and Gunicorn config into $(CONFIG_DIR)/
	@mkdir -p $(CONFIG_DIR)
	@if [ -f /etc/nginx/sites-available/todo ]; then cp /etc/nginx/sites-available/todo $(CONFIG_DIR)/; fi
	@if [ -f /etc/systemd/system/todocorn.service ]; then cp /etc/systemd/system/todocorn.service $(CONFIG_DIR)/; fi

push-deploy: 	## Push Nginx and Gunicorn config to system
	@echo $(CONFIG_DIR)
	@if [ -f $(CONFIG_DIR)/todo ]; then \
		sudo cp $(CONFIG_DIR)/todo /etc/nginx/sites-available/; \
		sudo ln -sf /etc/nginx/sites-available/todo /etc/nginx/sites-enabled/todo; \
		sudo systemctl restart nginx; \
	fi
	@if [ -f $(CONFIG_DIR)/todocorn.service ]; then \
		sudo cp $(CONFIG_DIR)/todocorn.service /etc/systemd/system; \
		sudo systemctl daemon-reload; \
		sudo systemctl restart todocorn; \
		sudo systemctl enable todocorn; \
	fi

run-gunicorn: install-gunicorn ## Run Gunicorn
	gunicorn -c gunicorn_config.py config.wsgi


reload-deploy: ## Reload $(CONFIG_DIR)
	sudo systemctl daemon-reload; \
	sudo systemctl restart todocorn; \
	sudo systemctl enable todocorn; \
	sudo systemctl restart nginx; 

install-nginx: ## Install Nginx
	./scripts/install-nginx.sh

install-gunicorn: ## Install Gunicorn
	poetry add gunicorn

install-db: ## Install Postgres
	./scripts/install-db.sh

setup-db: ## Create the database
	python scripts/setup-db.py > ./scripts/createdb.sql
	sudo -u postgres psql < ./scripts/createdb.sql
	rm ./scripts/createdb.sql # it contains sensitive information!


uninstall-nginx: ## Uninstall Nginx
	./scripts/uninstall-nginx.sh

uninstall-gunicorn: ## Uninstall Gunicorn
	./scripts/uninstall-gunicorn.sh

uninstall-db: ## Uninstall Postgres
	./scripts/uninstall-db.sh
