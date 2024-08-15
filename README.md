# django_todo



## Install poetry 
```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### Make virtual env in project
```sh
poetry config virtualenvs.in-project true
```

## Testing

```sh
curl -X POST -d "username=test&password=Asdf,mnb1234" http://127.0.0.1:8000/api-token-auth/

```


```sh
curl -H "Authorization: Token d2774892bb108cd133b78e431b02085b8517b20d" http://127.0.0.1:8000/api/todos/
```