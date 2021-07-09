from django.urls import path
from django.urls import include
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
]