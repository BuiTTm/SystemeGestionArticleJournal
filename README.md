# Système de gestion d'article de journal - Équipe 7

## Setup

1. Create [venv](https://docs.python.org/3/tutorial/venv.html): `python3 -m venv env`

2. Activate `venv`: `source env/bin/activate`

3. Install dependencies: `pip install -r requirements.txt`

4. Setup database: `docker-compose up -d`

5. Start server: `python manage.py runserver`

## Connect to the database

You can use a Adminer to explore your database at [http://localhost:3010](http://localhost:3010). Select PostgreSQL and enter the default credentials (postgres/example). Leave `db` as the value for Server, it connects through the Docker network.

You can also connect using `psql` in your terminal since we expose the database port to our machine: `psql -h localhost -p 5433 -U postgres`.
