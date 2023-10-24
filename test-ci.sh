#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python before running this script."
    exit 1 
fi

python3 -m pip install -r requirements-ci.txt

export exitcode=0

echo "Pylint Check"
find -name "*.py" -not -path "./tests/*" | xargs pylint --output-format=text

echo "Run Tests"
pytest -v --cov-report term --cov=sigl_api ./tests/

exit $exitcode
