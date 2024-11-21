# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the backend and frontend files into the container
COPY backend /app/backend
COPY frontend /app/frontend

# Install Python dependencies
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Expose the port that the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "/app/backend/app.py"]