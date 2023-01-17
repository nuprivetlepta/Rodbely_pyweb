from django.shortcuts import render

from django.views import View
from django.http import HttpResponse

class Hello(View):
    def get(self, request):
        greeting = """<h1>Hello, World</h1>"""
        return HttpResponse(greeting)