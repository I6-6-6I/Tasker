from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from .models import Worker, Task
# Create your views here.


def home(request):
    workers = Worker.objects.all()
    tasks = Task.objects.all()
    return render(request, "home.html", {"workers": workers, "tasks": tasks})


@require_http_methods(["POST"])
def addworker(request):
    name = request.POST["workername"]
    worker = Worker(name=name)
    worker.save()
    return redirect("home")


def deleteworker(request, worker_id):
    work = Worker.objects.get(id=worker_id)
    work.delete()
    return redirect("home")


@require_http_methods(["POST"])
def add(request):
    work = Worker.objects.get(id=request.POST["worker_id"])
    name = request.POST["title"]
    desc = request.POST["description"]
    task = Task(worker=work, title=name, description=desc)
    task.save()
    return redirect("home")


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    workers = Worker.objects.all()
    return render(request, 'edit.html', {'task': task, 'workers': workers})


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.status == 'TODO':
        task.status = 'In Progress'
    elif task.status == 'In Progress':
        task.status = 'Make It In Feature'
    elif task.status == 'Make It In Feature':
        task.status = 'Done'
    else:
        task.status = 'TODO'
    task.save()
    return redirect("home")


@require_http_methods(["POST"])
def updatetaskdata(request, task_id):
    task = Task.objects.get(id=task_id)
    task.worker = Worker.objects.get(id=request.POST["workers"])
    task.title = request.POST["title"]
    task.description = request.POST["description"]
    task.save()
    return redirect("home")


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("home")
