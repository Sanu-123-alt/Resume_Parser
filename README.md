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

## Limitations
- Only text-based PDF & DOCX parsing.
- Scanned PDFs not supported (no OCR).
- Extracted fields: name, email, phone, skills, experience.

## Setup
```bash
pip install -r requirements.txt
python manage.py runserver
