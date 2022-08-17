from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.index, name='index'),
    # path('login', views.auth, name='auth'),
    path('search/<str:query>', views.search, name='search'),
    path('tweet/<int:id>', views.show_tweet, name='show_tweet'),
]