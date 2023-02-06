from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from users.models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, "projects/index.html", context)


def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, "projects/project_list.html", context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, "projects/project_detail.html", context)


@login_required(login_url='login')
def project_create(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project-list')

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def project_update(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-list')

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project-list')
    context = {'project': project}
    return render(request, "projects/project_confirm_delete.html", context)