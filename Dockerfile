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
# RUN python manage.py collectstatic --noinput

# make migrations and migrate the database. 
# NOTE: this is not recommended in production. 
# In production, migrations should be part of deployment process.
RUN python manage.py makemigrations && python manage.py migrate

# Run the application:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]