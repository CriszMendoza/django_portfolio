from django.shortcuts import render
from .models import Proyect as Project

# Create your views here.


def render_home(request):
    projects = Project.objects.all()

    return render(request, 'home.html', {'projects': projects})
