# Pull the official base image
FROM python:3.10-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY apps /app/apps
COPY backend /app/backend
COPY manage.py /app/
COPY .env /app/

# collect static files
RUN python manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=backend.settings.production

# Expose the port that your app runs on
EXPOSE 8000

# Run the application:
CMD exec gunicorn backend.wsgi:application --bind :$PORT --workers 1 --threads 8 --timeout 0