build:
	@pip install -r requirements.txt

test: FORCE
	@pytest -v

cov:
	@pytest --cov-report term-missing --cov=xsniper tests

report: generate
	@pytest --cov-report annotate:reports --cov=xsniper tests
	@rm reports/xsniper___init__.py,cover
	@cat reports/*.py,cover

generate:
	@mkdir reports
lint:
	@pylint xsniper/*.py

FORCE:
