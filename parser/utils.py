import re
import spacy
from PyPDF2 import PdfReader
from docx import Document

nlp = spacy.load("en_core_web_sm")

def extract_text(file):
    if file.name.endswith('.pdf'):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    elif file.name.endswith('.docx'):
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    return ""


def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else ""

def extract_phone(text):
    match = re.search(r'(\+91[\s-]?\d{10}|\b\d{10}\b)', text)
    return match.group(0) if match else ""

def extract_name(text):
    lines = text.split('\n')
    
    for line in lines[:5]: 
        line = line.strip()
        if line and len(line.split()) <= 4:
            if "@" not in line and not any(char.isdigit() for char in line):
                return line.title()
    return ""

# def extract_name(text):
#     doc = nlp(text)
#     for ent in doc.ents:
#         if ent.label_ == "PERSON":
#             return ent.text
#     return ""

def extract_skills(text):
    skills_list = [
        "Python", "Django", "REST", "SQL",
        "JavaScript", "HTML", "CSS",
        "Machine Learning", "Git"
    ]
    found_skills = []
    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills
