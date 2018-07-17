from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from git import Repo

from front import repo
from front.models import (
    TaskSet,
    Task,
)


def logout_view(request):
    logout(request)
    return redirect('login')


def task_sets(request):
    user: User = request.user

    if not user.is_authenticated:
        return redirect('login')
    elif request.method == 'GET':
        task_sets_query = TaskSet.objects.filter(author=user).order_by('number')
        return render(
            request,
            'front/TaskSets.html',
            {
                'user': user,
                'tasksets': task_sets_query,
            }
        )


def task_set(request, number: int):
    if request.method == 'GET':
        try:
            taskset = TaskSet.objects.filter(author=request.user).get(number=number)
        except TaskSet.DoesNotExist:
            # todo create 404 error page (optional)
            return HttpResponse("<h1>PAGE NOT FOUND PLZ CREATE AN OBJECT:)</h1>")

        tasks_query = Task.objects.filter(task_set=taskset).order_by('number')

        return render(
            request,
            'front/TaskSet.html',
            {
                'user': request.user,
                'taskset': taskset,
                'tasks': tasks_query,
            }
        )


def index(request):
    return redirect('tasksets')


def test(request, number: int):
    user: User = request.user
    taskset: TaskSet = TaskSet.objects.get(number=number)

    result = []

    data = {
        'user': user,
        'taskset': taskset,
        'display': 'none',
        'results': result,
    }

    if request.method == 'GET':
        return render(
            request,
            'front/Test.html',
            data,
        )
    elif request.method == 'POST':
        tasks: list = list(Task.objects.filter(task_set=taskset).order_by('number'))

        url: str = request.POST.get('link')
        repository: Repo = repo.clone(url)

        data['results'] = [(t, repo.has_commit(repository, t)) for t in tasks]
        data['display'] = 'block'

        return render(
            request,
            'front/Test.html',
            data,
        )


def create_task_set(request):
    user: User = request.user

    if not user.is_authenticated:
        return redirect('login')
    elif request.method == 'GET':
        return render(
            request,
            'front/NewTaskSet.html',
            {
                'user': user,
            }
        )
    elif request.method == 'POST':
        number = TaskSet.objects.filter(author=user).count() + 1

        time_from = request.POST.get('time_from', '')
        time_to = request.POST.get('time_to', '')

        taskset = TaskSet(
            author=user,
            number=number,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            time_from=time_from,
            time_to=time_to,
        )
        taskset.save()
        return redirect('taskset/' + number)


def create_task(request, number: int):
    user: User = request.user
    if not user.is_authenticated:
        return redirect('login')
    elif request.method == 'GET':
        return render(
            request,
            'front/NewTask.html',
            {
                'user': user,
            }
        )
    elif request.method == 'POST':
        ts = TaskSet.objects.get(number=number)
        num = Task.objects.filter(task_set=task_set).count() + 1

        time_from = request.POST.get('time_from', '')  # todo parse date
        time_to = request.POST.get('time_to', '')

        task = Task(
            task_set=ts,
            number=num,
            title=request.POST.get('title', 'title'),
            description=request.POST.get('description', ''),
            time_to=time_to,
            time_from=time_from,
        )
        task.save()
