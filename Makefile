.PHONY: install virtualenv lint fmt test clean

TARGET_FILES=methods main.py src tests

install:
	@echo "Installing for dev environment"
	@poetry install --no-root

virtualenv:
	@echo "Creating virtual environment"
	@poetry env use python3

lint:
	@echo "Running linting"
	@poetry run flake8 ${TARGET_FILES}

fmt:
	@echo "Formatting code"
	@poetry run isort ${TARGET_FILES}
	@poetry run black --line-length 79 ${TARGET_FILES}

test:
	@echo "Running tests"
	@poetry run pytest -v --cov --cov-report=html --cov-report=term

clean:
	@echo "Cleaning up"
	@rm -rf .venv  # Remove virtual environment (if needed)
	@poetry run find . -name '__pycache__' -exec rm -r {} +  # Remove __pycache__ directories
	@poetry run find . -name '*.pyc' -exec rm {} +  # Remove .pyc files
