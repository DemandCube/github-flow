clean:
	rm -rf venv

setup:
	virtualenv venv
	echo "RUN:"
	echo ". venv/bin/activate"
	
install-dev:
	pip install --upgrade .

register:
	python setup.py register

publish:
	python setup.py sdist upload
	