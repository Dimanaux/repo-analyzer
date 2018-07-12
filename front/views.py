from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('../test/')


def login_page(request):
    return render(request, 'front/login.html', {})


def task_set(request):
    return render(request, 'front/TaskSet.html', {})


def index(request):
    # todo create main page
    return render(request, 'front/bitbucket.html', {})


def test(request):
    return render(request, 'front/test.html', {'user': request.user})


def profile_view(request):
    return redirect('index')


def students_list(request):
    return render(request, 'front/listOfStudents.html', {})
