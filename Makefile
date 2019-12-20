all: install

configure:
	@poetry install

test:
	@poetry run pytest --cov=gendiff tests/ 

lint:
	@poetry run flake8

selfcheck:
	@poetry check

check: selfcheck test lint

build: check
	@poetry build
