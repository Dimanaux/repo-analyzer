from django.shortcuts import render


# Create your views here.

def login(request):
    if request.method == 'POST':
        pass
        # todo: auth
    elif request.method == 'GET':
        return login_page(request)


def login_page(request):
    # todo: create login page
    return render(request, 'front/login.html', {})


def logout(request):
    # todo: logout
    return None
