from django.contrib import admin
from django.urls import path
from .views import ReturnRnd

urlpatterns = [
    path('rndnumber/', ReturnRnd.as_view()),
]
