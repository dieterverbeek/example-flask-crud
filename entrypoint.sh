#!/bin/bash

# Exit script als een commando faalt
set -e



# Voer database-migraties uit
flask db init || true  # init kan falen als de migraties al zijn gedaan
flask db migrate -m "entries table"  # Dit is je specifieke migratie voor 'entries table'
flask db upgrade  # Zorgt ervoor dat de database wordt bijgewerkt naar de laatste migraties

# Start Gunicorn om de Flask-applicatie te serveren
exec gunicorn -w 4 -b 0.0.0.0:8000 crudapp:app
