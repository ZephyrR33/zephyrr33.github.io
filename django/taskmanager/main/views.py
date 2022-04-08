from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def genres(request):
    return render(request, 'main/genres.html')


def favorites(request):
    return render(request, 'main/favorites.html')


def premium(request):
    return render(request, 'main/premium.html')

def ganres_week(request):
    return render(request, 'main/ganres_week.html')

def ganers_month(request):
    return render(request, 'main/ganers_month.html')



