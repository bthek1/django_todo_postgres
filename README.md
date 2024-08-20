# django_todo



## Installation
### poetry 
```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### Make virtual env in project
```sh
poetry config virtualenvs.in-project true
```
### Install direnv
```sh
sudo apt install direnv
```

### Install dependencies
```sh
poetry install
direnv allow
```

### Create .env file

### Install Postgres
```sh
make install_db
```

### Create superuser
```sh
make superuser
```


## RUN
```sh
make runserver
```


## Production
### Install Nginx, Gunicorn, Postgres
```sh
make install_nginx
make install_gunicorn
make install_db
```

### Migrate
```sh
make migrate
make push_deploy
```

### Create superuser
```sh
make superuser
```

### Go to IP/admin


## Testing

```sh
curl -X POST -d "username=test&password=Asdf,mnb1234" http://127.0.0.1:8000/api-token-auth/

```


```sh
curl -H "Authorization: Token d2774892bb108cd133b78e431b02085b8517b20d" http://127.0.0.1:8000/api/todos/
```