test:
	python -m pytest ./tests/

test-verbose:
	python -m pytest -vvs ./tests/

lint:
	pylint ./main
	pylint ./tests
