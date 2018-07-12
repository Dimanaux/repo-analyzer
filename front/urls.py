from django.contrib import admin

from . import views
from django.urls import path

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='front/login.html'), name='login'),

    path('accounts/profile/', views.profile_view),

    path('test/', views.test, name='test'),
    path('logout/', views.logout_view, name='logout'),

    # last pattern
    path('', views.index, name='index')
]
