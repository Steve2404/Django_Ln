from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request.get_host())
    return HttpResponse("Hello, world. You're at the polls index.")
