#!/bin/bash

# Создаем необходимые директории
mkdir -p logs
mkdir -p staticfiles
mkdir -p mediafiles

# Удаляем старые статические файлы
rm -rf staticfiles/*

# Собираем статические файлы
python manage.py collectstatic --noinput --clear

# Запускаем Gunicorn с настройками для статических файлов
gunicorn library.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120 \
    --access-logfile logs/access.log \
    --error-logfile logs/error.log \
    --log-level debug 