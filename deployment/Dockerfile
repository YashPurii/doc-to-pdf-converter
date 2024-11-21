# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file into the container first
COPY backend/requirements.txt /app/backend/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Copy the entire backend and frontend files into the container
COPY backend /app/backend
COPY templates /app/templates
COPY static /app/static

# Expose the port that the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "/app/backend/app.py"]
