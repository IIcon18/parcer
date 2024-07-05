# Используем официальный образ Python в качестве базового
FROM python:3.10-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы требований и устанавливаем зависимости проекта
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем все файлы проекта в контейнер
COPY backend /app/backend
COPY frontend /app/frontend

# Устанавливаем переменную окружения для Django
ENV DJANGO_SETTINGS_MODULE=Parser.settings

# Открываем порт для приложения
EXPOSE 8000

# Запускаем сервер
CMD ["sh", "-c", "python /app/backend/manage.py migrate && python /app/backend/manage.py runserver 0.0.0.0:8000"]
