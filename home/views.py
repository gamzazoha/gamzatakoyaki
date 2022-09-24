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

def place1(request):
    return render(request, 'category__place__1.html')

def food1(request):
    return render(request, 'category__food__1.html')

def reservation_pos(request):
    return render(request, 'reservation__possible.html')

def reservation_imp(request):
    return render(request, 'reservation__impossible.html')