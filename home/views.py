from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'homepage_1.html')

def food(request):
    return render(request, 'category__food.html')

def place(request):
    return render(request, 'category__place.html')

def beauty(request):
    return render(request, 'category__beauty.html')

