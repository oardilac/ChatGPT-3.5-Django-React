# Pull the official base image
FROM python:3.10-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY apps /app/apps
COPY backend /app/backend
COPY manage.py /app/
COPY .env /app/

RUN python manage.py collectstatic --no-input

# RUN python manage.py makemigrations && RUN python manage.py migrate

ENV DJANGO_SETTINGS_MODULE=backend.settings
ENV PORT=8000
EXPOSE $PORT

# Run the application:
CMD exec gunicorn backend.wsgi:application --bind 0.0.0.0:${PORT} --workers 1 --threads 8 --timeout 0