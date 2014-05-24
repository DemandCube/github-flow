clean:
	rm -rf venv
	rm -rf src/githubflow.egg-info

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
	
	
	