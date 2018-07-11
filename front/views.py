from django.shortcuts import render


# Create your views here.

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
    return None


def test(request):
    return render(request, 'front/test.html', {})