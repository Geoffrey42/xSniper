build:
	pip install -r requirements.txt

test: FORCE
	pytest -v

cov:
	pytest --cov=xSniper tests

lint:
	pylint xsniper/*.py

FORCE:
