from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import (
    extract_text,
    extract_email,
    extract_phone,
    extract_name,
    extract_skills
)

@api_view(['POST'])
def upload_and_parse_resume(request):
    file = request.FILES.get('resume')

    if not file:
        return Response({"error": "No file uploaded"}, status=400)

    text = extract_text(file)

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "experience": "Fresher" if "experience" not in text.lower() else "Experienced"
    }

    return Response(data)
