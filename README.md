# Système de gestion d'article de journal - Équipe 7

## Setup

1. Install Docker version 20.10.21 or newer

2. Start server: `docker compose up -d`

## Connect to the database

You can use a Adminer to explore your database at [http://localhost:3010](http://localhost:3010). Select PostgreSQL and enter the default credentials (postgres/example). Leave `db` as the value for Server, it connects through the Docker network.

You can also connect using `psql` in your terminal since we expose the database port to our machine: `psql -h localhost -p 5433 -U postgres`.
