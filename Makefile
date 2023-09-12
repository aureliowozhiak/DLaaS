.PHONY: install virtualenv lint fmt test clean

install:
	@echo "Installing for dev environment"
	@poetry install --no-root

virtualenv:
	@echo "Creating virtual environment"
	@poetry env use python3

lint:
	@echo "Running linting"
	@poetry run flake8 methods main.py tests

fmt:
	@echo "Formatting code"
	@poetry run isort methods main.py tests
	@poetry run black --line-length 79 methods main.py tests

test:
	@echo "Running tests"
	@poetry run pytest -v --cov --cov-report=html --cov-report=term

clean:
	@echo "Cleaning up"
	@rm -rf .venv  # Remove virtual environment (if needed)
	@poetry run find . -name '__pycache__' -exec rm -r {} +  # Remove __pycache__ directories
	@poetry run find . -name '*.pyc' -exec rm {} +  # Remove .pyc files
