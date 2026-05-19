#!/bin/bash

# Создаем необходимые директории
mkdir -p logs
mkdir -p staticfiles
mkdir -p mediafiles

# Собираем статические файлы
python manage.py collectstatic --noinput

# Запускаем Gunicorn
gunicorn -c gunicorn_config.py library.wsgi:application 