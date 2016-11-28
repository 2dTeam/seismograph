#!/usr/bin/env bash
python setup.py test
coverage run --branch --source seismograph setup.py test
coverage report
coverage html
