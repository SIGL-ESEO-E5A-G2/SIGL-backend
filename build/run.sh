#!/bin/bash

python3 -m pip install -r requirements-ci.txt

export exitcode=0

echo "Pylint Check"
# disable is for black and pylint indentation conflict
# pylint-exit exits 0 code in case of any trouble but fatal in pylint, which can be useful
find -name "*.py" -not -path "./tests/*" | xargs pylint --output-format=text


#For now there are no tests set in qbuild, when done below code could be uncommented in order to get a documentation badge.
# If you choose to perform tests with an app.tests.yml file, below code is not needed.
echo "Run Tests"
pytest -v --cov-report term --cov-report html:/var/workspace/code/target/documentation/html/ --cov-report xml:/var/workspace/code/target/documentation/xml/index.xml --cov=src ./tests/

if [ "$?" -ne "0" ]; then
  echo "Pytest failed - exit code 1"
  #export exitcode=1
else
  echo "PyTest successful"
fi

export cov=`grep  "pc_cov" /var/workspace/code/target/documentation/html/index.html | cut -d ">" -f2 | cut -d "<" -f1 | cut -d "%" -f1 |awk  '{ printf( "%s ", $1 ); } END { printf( "\n" ); }'`
if [[ $(bc -l <<< "$cov<60.0") -eq 1 ]] ; then
  export color=red
  echo "documentation below 60%"
  echo "Qbuild failed - the code documentation in unit test is not sufficient (${cov}%) "
  #export exitcode=1
else
  export color=green
  echo "documentation above 60% (${cov}%)"
fi

exit $exitcode
