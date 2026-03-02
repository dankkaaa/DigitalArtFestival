#!/usr/bin/env sh
set -e

echo "Waiting for Postgres..."
until python -c "import socket; s=socket.socket(); s.connect(('${POSTGRES_HOST}', int('${POSTGRES_PORT}'))); s.close()" 2>/dev/null
do
  sleep 0.5
done
echo "Postgres is up!"

python manage.py migrate --noinput
python manage.py collectstatic --noinput || true

python manage.py runserver 0.0.0.0:8000