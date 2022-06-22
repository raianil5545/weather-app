from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('users/', views.user_index, name="user.index"),
    path('users/login/', views.user_login, name='user.login'),
    path('users/register/', views.user_register, name='user.register'),
    path('users/logout/', views.user_logout, name='user.logout')
]