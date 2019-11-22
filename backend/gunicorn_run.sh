#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply master database migrations"
python manage.py migrate bookreaders 0001_initial
python manage.py migrate bookreaders 0001_initial --database=replica

python manage.py migrate
python manage.py migrate --database=replica


echo "Starting server"
exec gunicorn -w 3 --bind 0.0.0.0:8000 dj.wsgi:application