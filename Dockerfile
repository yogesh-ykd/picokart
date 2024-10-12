# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the current project directory into the container
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Run Django management commands for migrations and collectstatic
RUN python picokart/manage.py makemigrations \
    && python picokart/manage.py migrate \
    && python picokart/manage.py collectstatic --noinput

# Command to run Django's development server
CMD ["python", "picokart/manage.py", "runserver", "0.0.0.0:8000"]
