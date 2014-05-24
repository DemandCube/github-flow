clean:
	rm -rf venv

setup:
	virtualenv venv
	echo "RUN:"
	echo ". venv/bin/activate"
	
install-dev:
	pip install --upgrade .
	

	