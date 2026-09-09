from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
from .models import Project

def home(request):
    projects = Project.objects.all()

    return render(request, "home.html", {
        "projects": projects
    })