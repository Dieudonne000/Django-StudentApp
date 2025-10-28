# schoolApp

A small Django project for managing simple school-related data (students, classes, teachers). This repository contains the minimal code and configuration to run and develop the app locally.

## Requirements
- Python 3.8+
- Django 3.2+ (or the version specified in requirements.txt)
- pip

## Quick start (Windows)
1. Open a terminal in:
    C:/Users/Dieudonne/Documents/RCA/Django-work/schoolApp
2. Create and activate a virtual environment:
    - python -m venv .venv
    - .venv\Scripts\activate
3. Install dependencies:
    - pip install -r requirements.txt
4. Apply migrations and create a superuser:
    - python manage.py migrate
    - python manage.py createsuperuser
5. Run the development server:
    - python manage.py runserver
6. Open http://127.0.0.1:8000 in your browser.

## Project structure (typical)
- manage.py
- schoolApp/ (project settings)
- app/ or apps/ (Django apps: students, teachers, etc.)
- templates/
- static/
- requirements.txt
- README.md

Adjust names if your apps differ.

## Development notes
- Add new models, then run makemigrations and migrate.
- Use the admin site to manage data during development.
- Keep secrets out of the repository (use environment variables or a .env file).

## Contributing
- Create feature branches, keep commits focused, open PRs against main branch.
- Run tests locally before opening a PR.

