# Booksite Project

## Запуск локально

1. Установите зависимости:

```bash
python -m pip install -r requirements.txt
```

2. Выполните миграции:

```bash
python manage.py migrate
```

3. (Опционально) Загрузите тестовые данные:

```bash
python manage.py load_initial_data
```

4. Запустите сервер разработки:

```bash
python manage.py runserver
```

Локальный сайт будет доступен по адресу: http://127.0.0.1:8000/
