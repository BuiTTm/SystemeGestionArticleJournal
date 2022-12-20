# Système de gestion d'article de journal - Équipe 7

## Setup

1. Install Docker version 20.10.21 or newer and Docker-compose

2. Start server: `docker compose up -d`. This will also migrate the database.

3. Seed the database with default data:

```
docker exec -it projet-web-1 bash
python manage.py loaddata seed-data.json
```

4. Now you can login using one of these users

```
## ADMIN
admin@mgl7361.com
motdepasse123

## ÉVALUATEUR 1
evaluateur1@mgl7361.com
motdepasse123

## ÉVALUATEUR 2
evaluateur2@mgl7361.com
motdepasse123

## ÉVALUATEUR 3
evaluateur3@mgl7361.com
motdepasse123

## AUTEUR 1
auteur1@mgl7361.com
motdepasse123

## AUTEUR 2
auteur2@mgl7361.com
motdepasse123
```

The project will be accessible at http://localhost:8000.

## Contributing

### Connect to the database

You can use a Adminer to explore your database at [http://localhost:3010](http://localhost:3010). Select PostgreSQL and enter the default credentials (postgres/example). Leave `db` as the value for Server, it connects through the Docker network.

You can also connect using `psql` in your terminal since we expose the database port to our machine: `psql -h localhost -p 5433 -U postgres`.

### Run commands

You can then connect to the container if you need to ran commands like `python manage.py migrate` or `python manage.py createsuperuser`. To do so, enter the container using: `docker exec -it projet-web-1 bash`.
