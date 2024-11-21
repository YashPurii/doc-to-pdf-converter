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
