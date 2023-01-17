from django.contrib import admin
from django.urls import path
from .views import Forma

urlpatterns = [
    path('login/', Forma.as_view()),
]
