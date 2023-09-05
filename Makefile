test:
	python -m coverage run -m unittest discover && python -m coverage html --omit="test_*.py,__init__.py"