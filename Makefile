.PHONY: test
test:
	$(MAKE) mypy && $(MAKE) pytest

.PHONY: mypy
mypy:
	poetry run mypy examples

.PHONY: pytest
pytest:
	poetry run pytest
