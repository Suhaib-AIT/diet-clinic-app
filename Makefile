dev-up:
docker-compose up --build

lint:
ruff backend

format:
black backend

test:
pytest backend/tests

seed-db:
docker-compose run backend python seed.py
