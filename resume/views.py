from django.shortcuts import render
from .models import Experience, Education, Language, Skill

# Create your views here.
def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    languages = Language.objects.all()
    skills = Skill.objects.all()
    resumes = {'experiences': experiences,'educations':educations, 'languages':languages, 'skills':skills}
    return render(request, "resume.html", resumes)