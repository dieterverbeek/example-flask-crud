#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Run the database migrations
flask db init || true  # init command kan falen als de migrations folder al bestaat
flask db migrate -m "Initial migration"
flask db upgrade

# Start the Gunicorn server
exec gunicorn app:app -b 0.0.0.0:8000
