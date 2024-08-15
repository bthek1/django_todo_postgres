.PHONY: help pull-deploy push-deploy makemigrations migrate runserver createsuperuser collectstatic test install-nginx uninstall-nginx install-gunicorn uninstall-gunicorn

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

createsuperuser: ## Create a superuser
	poetry run python manage.py createsuperuser

collectstatic: ## Collect static files
	poetry run python manage.py collectstatic --noinput

test: ## Run tests
	poetry run python manage.py test

install-nginx: ## Install Nginx
	sudo apt update
	sudo apt install -y nginx

uninstall-nginx: ## Uninstall Nginx
	sudo systemctl stop nginx
	sudo apt remove --purge nginx nginx-common nginx-full
	sudo rm -rf /etc/nginx
	sudo rm -rf /var/www/html
	sudo rm -rf /var/log/nginx
	sudo rm -rf /usr/sbin/nginx
	sudo rm -rf /usr/share/nginx
	sudo apt autoremove -y
	sudo systemctl daemon-reload

install-gunicorn: ## Install Gunicorn
	poetry add gunicorn

run-gunicorn: install-gunicorn ## Run Gunicorn
	gunicorn -c gunicorn_config.py config.wsgi


uninstall-gunicorn: ## Uninstall Gunicorn
	sudo systemctl stop gunicorn
	sudo systemctl disable gunicorn
	sudo rm /etc/systemd/system/gunicorn.service
	sudo systemctl daemon-reload
	poetry remove gunicorn


pull-deploy: 	## Pull Nginx and Gunicorn config into deploy/
	@mkdir -p deploy
	@if [ -f /etc/nginx/sites-available/todo ]; then cp /etc/nginx/sites-available/todo deploy/; fi
	@if [ -f /etc/systemd/system/gunicorn.service ]; then cp /etc/systemd/system/gunicorn.service deploy/; fi

push-deploy: 	## Push Nginx and Gunicorn config to system
	@if [ -f deploy/todo ]; then \
		sudo cp deploy/todo /etc/nginx/sites-available/; \
		sudo ln -sf /etc/nginx/sites-available/todo /etc/nginx/sites-enabled/todo; \
		sudo systemctl restart nginx; \
	fi
	@if [ -f deploy/gunicorn.service ]; then \
		sudo cp deploy/gunicorn.service /etc/systemd/system; \
		sudo systemctl daemon-reload; \
		sudo systemctl restart gunicorn; \
		sudo systemctl enable gunicorn; \
	fi

reload-deploy: ## Reload deploy
	sudo systemctl daemon-reload; \
	sudo systemctl restart gunicorn; \
	sudo systemctl enable gunicorn; \
	sudo systemctl restart nginx;