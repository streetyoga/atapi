all:
	$(error please pick a target)

env:
	test -d env || python3 -m venv env
	./env/bin/python3 -m pip install -r requirements.txt


dev-env: env
	./env/bin/python3 -m pip install -r requirements-dev.txt

test:
	find . -name '*.pyc' -exec rm -f {} \;
	./env/bin/flake8 atf tests
	./env/bin/python3 -m pytest \
	    --doctest-modules \
	    --disable-warnings \
	    --verbose \
	    atf tests
