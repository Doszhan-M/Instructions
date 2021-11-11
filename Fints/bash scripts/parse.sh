#!/bin/bash

cd ../
cd ../
source venv/bin/activate
celery -A slackbot worker -l INFO