import multiprocessing

# Количество рабочих процессов
workers = multiprocessing.cpu_count() * 2 + 1

# Путь к WSGI приложению
wsgi_app = "library.wsgi:application"

# Хост и порт
bind = "127.0.0.1:8000"

# Таймауты
timeout = 120
keepalive = 5

# Логирование
accesslog = "logs/access.log"
errorlog = "logs/error.log"
loglevel = "info"

# Перезагрузка при изменении кода
reload = True

# Предзагрузка приложения
preload_app = True 