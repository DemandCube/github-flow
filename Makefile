# make help
# @ surpresses the output of the line
help:
	@make -qp | awk -F':' '/^[a-zA-Z0-9][^$$#\/\t=]*:([^=]|$$)/ {split($$1,A,/ /);for(i in A)print A[i]}'

# raw to commandline execute
# make -qp | awk -F':' '/^[a-zA-Z0-9][^$#\/\t=]*:([^=]|$)/ {split($1,A,/ /);for(i in A)print A[i]}' 

clean:
	rm -rf venv
	rm -rf src/githubflow.egg-info
	rm -rf dist

setup:
	virtualenv venv
	echo "RUN:"
	echo ". venv/bin/activate"

# installs as a local package
install-local:
	pip install --upgrade .

# installs editable in place
install-dev:
	pip install -e .

# installs from the pypi repo
install:
	pip install githubflow

register:
	python setup.py register

publish:
	python setup.py sdist upload

# Run as `make ARGS="--version" debug`
debug:
	PYTHONPATH="${PYTHONPATH}:./src" python -m pdb src/githubflow/runner.py $(ARGS)