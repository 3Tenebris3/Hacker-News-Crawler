.PHONY: install run dev test lint format docker

install:
	poetry install

run:
	poetry run uvicorn src.main:app --reload

dev: lint test

test:
	poetry run pytest -q

lint:
	poetry run ruff check src tests

format:
	poetry run ruff format .

docker:
	docker compose up --build
