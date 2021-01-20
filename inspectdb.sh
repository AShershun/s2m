#!/bin/bash

source .venv/bin/activate
python manage.py inspectdb > models.py
