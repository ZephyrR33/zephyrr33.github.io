from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs


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
    return render(request, 'main/homeless_god/episode-1.html')


def dor1(request):
    return render(request, 'main/dororo/episode-1.html')


def mb1(request):
    return render(request, 'main/magic_battle/episode-1.html')


def opm1(request):
    return render(request, 'main/onepunchman/episode-1.html', {'url': url_punch_season1_ep_1()[0]['episode1']['res1080']})


# парсер с ссылками на аниме (конкретно здесь сейчас ванпанчмен)
def url_punch_season1_ep_1():
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36', 
    'accept': '*/*'
    }
    page = 1
    counter = 1
    series = []
    urls = []
    season = 1
    while counter < 13:
        URL = f'https://jut.su/one-punchman/season-1/episode-{page}.html'
    
        r = requests.get(URL, headers=HEADERS, params = None)
        soup = bs(r.content, 'html.parser')
        items = soup.findAll('div', class_='videoContent')
        for item in items:
            for link in item.find_all('source'):
                link1 = link.get('src')
                urls.append(link1)
            
        series.append({
            f'episode{page}': {'res1080': urls[0],
            'res720': urls[1],
            'res480': urls[2],
            'res360': urls[3]
                }
        })
        
        urls.clear()
        counter += 1
        page += 1
    return series
    


