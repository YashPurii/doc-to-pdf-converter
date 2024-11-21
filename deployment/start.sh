#!/bin/bash

# Build the Docker image
echo "Building Docker image..."
docker build -t doc-to-pdf:latest .

# Check if an old container is running and stop it
if [ $(docker ps -q -f name=doc-to-pdf) ]; then
  echo "Stopping existing container..."
  docker stop doc-to-pdf
fi

# Remove the old container if it exists
if [ $(docker ps -aq -f name=doc-to-pdf) ]; then
  echo "Removing old container..."
  docker rm doc-to-pdf
fi

# Run the Docker container
echo "Starting a new container..."
docker run -d -p 5000:5000 --name doc-to-pdf doc-to-pdf:latest

# Display logs
echo "Application logs:"
docker logs -f doc-to-pdf
