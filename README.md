# Doc-to-PDF Converter

A web application that allows users to upload `.docx` files, view metadata, convert them to PDF (with optional password protection), and download the generated PDF. This project is designed with a user-friendly frontend, a Flask-based backend, and is fully containerized for easy deployment.

---

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
   - [Running Locally](#running-locally)
   - [Running with Docker](#running-with-docker)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Deployment](#deployment)
   - [Using Docker](#using-docker)
   - [Using Kubernetes](#using-kubernetes)
7. [Future Enhancements](#future-enhancements)
8. [Contributing](#contributing)
9. [License](#license)

---

## Features

- Upload `.docx` files for processing.
- Extract and display metadata (author, created date, etc.) of uploaded files.
- Convert `.docx` files to PDF with optional password protection.
- Download the generated PDF file.
- Responsive and modern user interface.
- Containerized with Docker for easy deployment.
- Kubernetes manifest for scalable deployment in a cluster.

---

## Technologies Used

- **Backend:** Python, Flask
- **PDF Processing:** python-docx, PyPDF2, reportlab
- **Frontend:** HTML, CSS, JavaScript
- **Containerization:** Docker
- **Orchestration:** Kubernetes
- **CI/CD Pipeline:** GitHub Actions

---

## Installation

### Running Locally

#### Prerequisites

1. Python 3.10 or higher installed.
2. `pip` (Python package manager).

#### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-repo-name>.git
   cd doc-to-pdf-converter
2. Install dependencies:
   '''bash
   pip install -r backend/requirements.txt
3. Run the application:
   '''bash
   python backend/app.py
4. Open the app in your browser:
   '''bash
   http://localhost:5000

---

### Running with Docker

#### Prerequisites

1. Docker installed on your system.
2. Docker Desktop running (on Windows/macOS).

#### Steps

1. Build the Docker image:
   ```bash
   docker build -t doc-to-pdf:latest .
2. Run the container:
   '''bash
   docker run -d -p 5000:5000 --name doc-to-pdf doc-to-pdf:latest
3. Open the app in your browser:
   '''bash
   http://localhost:5000

## Deployment

### Using Docker

1. **Build the Docker image:**
   ```bash
   docker build -t doc-to-pdf:latest .
2. **Run the Docker container:**
   '''bash
   docker run -d -p 5000:5000 --name doc-to-pdf doc-to-pdf:latest

### Using Kubernetes

1. **Push the Docker image to a container registry (e.g., Docker Hub):**
   ```bash
   docker tag doc-to-pdf <your-dockerhub-username>/doc-to-pdf:latest
   docker push <your-dockerhub-username>/doc-to-pdf:latest
   
2. **Apply the Kubernetes Manifest**
   '''bash
   kubectl apply -f deployment/kubernetes_manifest.yaml

3. **Deployment**
   ```bash
   kubectl get pods
   kubectl get services