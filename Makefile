test:
	$(MAKE) mypy

mypy:
	poetry run mypy examples
