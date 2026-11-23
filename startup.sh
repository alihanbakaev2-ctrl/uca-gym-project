#!/bin/sh
set -eu
cd /workspace
node scripts/preview.mjs stop || true
if curl -sf -o /dev/null --max-time 2 http://127.0.0.1:8080/; then
  exit 0
fi
cd /workspace/campus_gym
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
  .venv/bin/pip install -r requirements.txt
fi
.venv/bin/python manage.py migrate --noinput >>/tmp/app-startup.log 2>&1
.venv/bin/python manage.py runserver 0.0.0.0:8080 >>/tmp/app-startup.log 2>&1 &
