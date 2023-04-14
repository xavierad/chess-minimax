PYTHON_VERSION="3.10"

# pytest -n 3 tests/test_event_list.py

mypy:
	mypy board tests --config-file mypy.ini --python-version=${PYTHON_VERSION}