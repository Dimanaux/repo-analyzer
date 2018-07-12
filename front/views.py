from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('../test/')


def login_page(request):
    return render(request, 'front/login.html', {})


def login(request):
    method: str = request.method
    if method == 'POST':
        pass
        # todo
    elif method == 'GET':
        return login_page(request)


def index(request):
    # todo create main page
    return redirect('test/')


def test(request):
    return render(request, 'front/test.html', {'user': request.user})


def profile_view(request):
    return redirect('index')