#!/bin/bash

VERSIONS="3.6 3.7 3.8 3.9"
for VERSION in $VERSIONS
	do
		python3 -m virtualenv --python=python$VERSION venv$VERSION
		source venv$VERSION/bin/activate
		pip install -r requirements.txt
		python$VERSION --version
		python$VERSION setup.py test
		if [[ $? == 1 ]]; then
			exit 1
		fi;
		deactivate
done
python3 -m pip install twine wheel
python3 setup.py sdist bdist_wheel
python3 -m twine upload -u __token__ -p $TEST_TOKEN --non-interactive --repository testpypi dist/*
python3 -m twine upload -u __token__ -p $LIVE_TOKEN --non-interactive dist/*
