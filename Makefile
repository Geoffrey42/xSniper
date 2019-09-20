build:

test: FORCE

cov:

report: generate
	@pytest --cov-report annotate:reports --cov=xsniper tests
	@rm reports/xsniper___init__.py,cover
	@cat reports/*.py,cover

generate:
	@mkdir reports
lint:

FORCE:
