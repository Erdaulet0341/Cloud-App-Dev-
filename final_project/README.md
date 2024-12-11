# Django Application

Welcome to the Django Application! This guide will walk you through setting up and running the project.

## Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.7 or higher)
- pip (Python package manager)
- virtualenv (optional, but recommended)

## Getting Started

Follow the steps below to get the project up and running.

### 1. Clone the Repository

To get a copy of the code, run the following command:

```bash
git clone https://github.com/Erdaulet0341/Cloud-App-Dev-.git
cd Cloud-App-Dev-
cd final_project
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

Install the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

Apply database migrations to set up the database schema:

```bash
python manage.py migrate
```

### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000`.
