#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python before running this script."
    exit 1 
fi

read -p "Have you correctly configured Django with access to your local MySQL and started it? (y/n): " user_response


if [[ $user_response =~ ^[Yy](es)?$ ]]; then
    echo "Proceeding with the script..."
else
    echo "Please configure Django with access to your local MySQL and start it before running this script."
    exit 1
fi

sudo apt-get install libmysqlclient-dev

python3 -m pip install -r requirements.txt

export exitcode=0

echo "----------------------------------------"
echo "Pylint checks ..."
echo "----------------------------------------"

find -name "*.py" -not -path "./tests/*" | xargs pylint --output-format=text --disable=C0301,C0114,C0115,C0116,C0304,R0903

echo "----------------------------------------"
echo "Pylint checks completed. Running Tests..."
echo "----------------------------------------"

python3 manage.py test api

echo "----------------------------------------"
echo "Running Tests completed. End."
echo "----------------------------------------"

exit $exitcode
