#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Install Requirements
pip install -r requirements.txt

# 2. Collect Static Files
python manage.py collectstatic --no-input

# 3. Migrate Database
python manage.py migrate

# 4. Create Superuser (Corrected Syntax)
# We use single brackets [ ] which works in all shells
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
    python manage.py createsuperuser --no-input || true
fi