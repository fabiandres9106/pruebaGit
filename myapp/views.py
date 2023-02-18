from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

#Import forms
from .forms import CreateNewTask, CreateNewProject

#Import models
from .models import Project, Task

# Create your views here.

def index(request):
    title = 'Django Course!'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    return HttpResponse('Hello %s' % username)

def about(request):
    username = 'Fabian'
    return render(request, 'about.html', {
        'username': username
    }) 

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })

def task(request):
    #task= get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
         return render(request, 'tasks/create_task.html',{
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')
       