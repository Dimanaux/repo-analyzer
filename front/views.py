from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

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
    elif request.method == 'POST':
        number = TaskSet.objects.filter(author=user).count() + 1
        taskset = TaskSet(
            author=user,
            number=number,

            title=request.POST.get('title'),  # todo
            description=request.POST.get('description'),  # todo

            time_from=request.POST.get('time_from'),  # todo
            time_to=request.POST.get('time_to'),  # todo
        )
        taskset.save()
        return redirect('taskset/' + number)


def task_set(request, number: int):
    if request.method == 'GET':
        try:
            taskset = TaskSet.objects.filter(author=request.user).get(number=number)
        except TaskSet.DoesNotExist:
            # todo create 404 error page
            # todo optional
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
    elif request.method == 'POST':
        # todo create task

        task = Task(
            task_set=TaskSet.objects.get(number=number),

            title=request.POST.get('title'),  # todo
            description=request.POST.get('description'),  # todo

            time_to=request.POST.get('time_to'),  # todo
            time_from=request.POST.get('time_from'),  # todo
        )

        task.save()


def index(request):
    return redirect('tasksets')


def test(request):
    if request.method == 'GET':
        return render(
            request,
            'front/test.html',
            {
                'user': request.user,
            }
        )
    elif request.method == 'POST':
        # todo test
        pass
