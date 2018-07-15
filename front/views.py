from django.contrib.auth import logout
from django.shortcuts import render, redirect

from front.models import (
    TaskSet
)


def logout_view(request):
    logout(request)
    return redirect('index')


def task_sets(request):
    task_sets_query = TaskSet.objects.filter(author=request.user).order_by('number')
    return render(
        request,
        'front/TaskSets.html',
        {
            'user': request.user,
            'tasksets': task_sets_query,
        }
    )


def task_set(request, number: int):
    taskset = TaskSet.objects.filter(author=request.user).get(number=number)
    return render(
        request,
        'front/TaskSet.html',
        {
            'user': request.user,
            'taskset': taskset,
        }
    )


def index(request):
    return redirect('tasksets')


def test(request):
    # todo
    return render(
        request,
        'front/test.html',
        {
            'user': request.user,
        }
    )
