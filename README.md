# Sample Flask App

## Goals

* [x] Build a Hello World
* [x] [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy) or run locally: `heroku local`
* [x] Work with JSON
* [x] Explore custom commands

## Examples

### `GET /`

```sh
curl --request GET \
  --url http://localhost:5000
```

### `GET /echo`

```sh
curl --request GET \
  --url http://localhost:5000/echo \
  --header 'Content-Type: application/json' \
  --data '{"hello": "world"}'
```

### `say_hi` Command
```sh
pipenv run flask say_hi Leonel
```
```
Hello Leonel
```
