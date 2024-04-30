from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect


def home(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
            pass
    return render(request, 'registration/login.html')


def custom_logout(request):
    logout(request)
    return redirect('login')


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'job_detail.html', {'job': job})


def job_add(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'job_form.html', {'form': form})


def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'job_form.html', {'form': form})


def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'job_delete.html', {'job': job})


def job_filter(request):
    # Implement filtering logic based on user input
    # Example: filtered_jobs = Job.objects.filter(category__name='Software Development')
    return render(request, 'job_filter.html', {'filtered_jobs': filtered_jobs})
