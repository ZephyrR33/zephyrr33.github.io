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


def genres_week(request):   #фильтр на странце 'genres'
    return render(request, 'main/genres_week.html')


def genres_mounth(request):  #фильтр на странце 'genres'
    return render(request, 'main/genres_mounth.html')
    

def dororo_main(request):
    return render(request, 'main/dororo_main.html')


def homeless_god_main(request):
    return render(request, 'main/homeless_god_main.html')


def magic_battle_main(request):
    return render(request, 'main/magic_battle_main.html')


def onepunchman_main(request):
    return render(request, 'main/onepunchman_main.html')


def the_promised_neverland(request):
    return render(request, 'main/the_promised_neverland.html')


def tpn1(request):
    return render(request, 'main/the_promised_neverland/episode-1.html')


def hg1(request):
    return render(request, 'main/homeless_god_main/episode-1.html')

