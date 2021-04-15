#!/bin/bash
python3 -m virtualenv --python=python3.8 venv
source venv/bin/activate
python3 --version
python3 -m pip install -r requirements.txt
python3 -m pytest
