from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login),

    path('test/', views.test),

    # last pattern
    path('', views.index, name='index')
]
