# Dockerfile для Django Backend
# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода проекта
COPY . .

# Команда запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]