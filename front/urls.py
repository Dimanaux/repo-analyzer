from django.contrib.auth import views as auth_views
from django.urls import path

from front import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='front/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('tasksets/', views.task_sets, name='tasksets'),
    path('tasksets/<int:number>/', views.task_set, name='taskset'),
    path('tasksets/<int:number>/test/', views.test, name='test'),

    # last pattern
    path('', views.index, name='index'),
]
