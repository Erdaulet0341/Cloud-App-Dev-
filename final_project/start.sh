#!/bin/bash

cd final

export DJANGO_SETTINGS_MODULE="final_project.settings"


python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn final_project.wsgi:application --timeout 200 --log-level=debug --bind 0.0.0.0:8000