from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = get_object_or_404(Project, id=pk)
    return render(request, 'projects/single_project.html', {'project': project})

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user  # Assuming an owner field exists
            project.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def updateProject(request, pk):
    project = get_object_or_404(Project, id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
