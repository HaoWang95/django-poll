from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def index(request: HttpRequest):
    print(request.get_full_path_info())
    return HttpResponse("Polls Index")