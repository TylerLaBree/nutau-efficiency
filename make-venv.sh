#!/bin/bash
# Tyler LaBree
# Northern Illinois University

python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install pyroot jupyterlab urllib3==1.26.6

