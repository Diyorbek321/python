from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    return render(request, 'home.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def contact(request):
    return render(request, 'contact.html')

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})