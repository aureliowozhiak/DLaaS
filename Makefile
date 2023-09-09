.PHONY: install virtualenv lint fmt test clean

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -r requirements.dev.txt

virtualenv:
	@echo "Creating virtual environment"
	@python3 -m venv .venv

lint:
	@.venv/bin/pflake8 methods main.py

fmt:
	@.venv/bin/isort methods main.py
	@.venv/bin/black --line-length 79 methods main.py

test:
	@.venv/bin/pytest -v