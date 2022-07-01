#!/bin/sh

export APP_MODULE=${APP_MODULE-backend:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}

exec uvicorn --host $HOST --port $PORT "$APP_MODULE"
