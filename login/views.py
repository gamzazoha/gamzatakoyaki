from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def signup(request):
    return HttpResponse("signup page")

def login(request):
    return HttpResponse("login page")

def home(request):
    return HttpResponse("home page")