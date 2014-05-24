clean:
	rm -rf venv

setup:
	virtualenv venv
	echo "RUN:"
	echo ". venv/bin/activate"
	
install-local:
	pip install --upgrade .

install-dev:
	pip install -e .

register:
	python setup.py register

publish:
	python setup.py sdist upload
	