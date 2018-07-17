from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView

from front import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='front/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', RedirectView.as_view(url='/tasksets/')),

    path('register/', views.register, name='register'),

    path('tasksets/', views.task_sets, name='tasksets'),
    path('tasksets/new/', views.create_task_set, name='create_task_set'),

    path('tasksets/<int:number>/', views.task_set, name='taskset'),
    path('tasksets/<int:number>/new/', views.create_task, name='create_task'),
    path('tasksets/<int:number>/test/', views.test, name='test'),

    # last pattern
    path('', RedirectView.as_view(url='/tasksets/'), name='index'),
]
