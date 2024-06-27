#!/bin/bash
echo ">>> installing required packages..."
pip install pandas
pip install numpy
pip install requests
pip install sqlalchemy
pip install unittest2

echo ">>> running the tests ..."
if python ./automated_test.py; then 
  echo ">>> tests ran successfully..."
else 
  echo ">>> tests failed..."
fi