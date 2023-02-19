from django.contrib import admin
from django.urls import path
from .views import Forma

urlpatterns = [
    path('auth_shop/', Forma.as_view()),
]
