# Resume Parser API

This project is a Django REST API that parses resumes (PDF/DOCX) and extracts
basic candidate details such as name, email, phone, skills, and experience.

## Features
- Resume upload API
- PDF & DOCX support
- Automatic data extraction
- REST API responses

## Tech Stack
- Django
- Django REST Framework
- spaCy
- PyPDF2
- python-docx

## Setup
```bash
pip install -r requirements.txt
python manage.py runserver
