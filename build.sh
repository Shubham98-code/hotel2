#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Install Requirements
pip install -r requirements.txt

# 2. Collect Static Files (CSS/JS)
python manage.py collectstatic --no-input

# 3. Migrate Database (Fixes the 500 Error by creating tables)
python manage.py migrate

# 4. Create Superuser automatically (from Environment Variables)
# The "|| true" part prevents the build from failing if the user already exists
if [[ -n "$DJANGO_SUPERUSER_USERNAME" ]]; then
    python manage.py createsuperuser --no-input || true
fi