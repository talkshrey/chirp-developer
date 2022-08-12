from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.index, name='index'),
    path('login', views.auth, name='auth'),
]