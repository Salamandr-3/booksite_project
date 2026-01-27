# Booksite Project

## Запуск локально

### Вариант 1: Docker Compose

1. Скопируйте пример окружения:

```bash
cp .env.example .env
```

2. Соберите и запустите сервисы:

```bash
docker compose up --build
```

Сайт будет доступен по адресу: http://localhost:8080/

### Вариант 2: запуск без Docker

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
