#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Install requirements
pip install -r requirements.txt

# Switch to frontend directory to run npm commands
cd frontend

# Install node modules
npm install

# Build frontend application
npm run build

# Switch back to parent directory
cd ..

# Run database migrations
python manage.py migrate --noinput

# Load initial data for categories
python manage.py loaddata categories

# Collect static files
python manage.py collectstatic --noinput -i admin -i rest_framework

# Run gunicorn server
gunicorn wsgi:application --bind 0.0.0.0:8000
