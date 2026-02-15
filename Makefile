# Makefile

# Makefile for SkyNet project

.PHONY: install run test lint format

install:
	pip install -r backend/requirements.txt

run:
	uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest backend/tests

lint:
	flake8 backend/app

format:
	black backend/app

frontend-install:
	cd frontend && npm install

frontend-run:
	cd frontend && npm start

frontend-test:
	cd frontend && npm test

frontend-lint:
	cd frontend && eslint src/**/*.ts src/**/*.tsx

frontend-format:
	cd frontend && prettier --write src/**/*.ts src/**/*.tsx