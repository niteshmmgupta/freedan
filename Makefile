.PHONY: test clean env check-testdata-uptodate regenerate run
.DELETE_ON_ERROR:

# build directory 
BUILDDST=${PWD}/build
# python virtualenv location
ENV=$(BUILDDST)/.env
# python interpreter to use
BASE_PYTHON=python3
PYTHON=$(ENV)/bin/python
# requirements location
REQUIREMENTS=requirements.txt
# location of python code
PYTHON_SRC=*.py
# Longest python line, TODO 100
MAX_LINE=133
# hide __pycache__
export PYTHONDONTWRITEBYTECODE=true

# runs linter, compiler, and security checks
test: env
	bash -c "set -ex; $(PYTHON) -m compileall -f $(PYTHON_SRC)"
	bash -c "set -ex; $(PYTHON) -m pylint -E $(PYTHON_SRC)"
	bash -c "set -ex; $(PYTHON) -m pycodestyle --show-source --show-pep8 --max-line-length=$(MAX_LINE) $(PYTHON_SRC)"
	bash -c "set -ex; $(PYTHON) -m bandit -c bandit.yml -lll -r $(PYTHON_SRC)"

# start program interactively
run: env
	bash -c "set -ex; $(PYTHON) freedan.py --interactive"

# remove all artifacts
clean:
	rm -rf $(BUILDDST)

env: $(ENV)/bin/activate
$(ENV)/bin/activate: Makefile $(REQUIREMENTS) 
	# delete existing, if any, virtual environments
	rm -rf $(ENV)
	# create a virtual environment
	$(BASE_PYTHON) -m venv $(ENV)
	# install requirements into virtual environment
	$(ENV)/bin/pip install --no-input -U -r $(REQUIREMENTS) 
	touch $(ENV)/bin/activate

