
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

django.setup()

from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
from django_user_agents.utils import get_user_agent

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


def tower_of_god_main(request):
    return render(request, 'main/tower_of_god_main.html')


def onepunchman_main(request):
    return render(request, 'main/onepunchman_main.html')


def tokyo_avengers_main(request):
    return render(request, 'main/tokyo_avengers_main.html')






    




#omepunchman 1 season
def opm1_1(request):
    return render(request, 'main/onepunchman/season-1/episode-1.html')#, {'url': url_punch_season1_ep_1()[0]['episode1']['res1080']})


def opm2_1(request):
    return render(request, 'main/onepunchman/season-1/episode-2.html')#, {'url': url_punch_season1_ep_1()[1]['episode2']['res1080']})    


def opm3_1(request):
    return render(request, 'main/onepunchman/season-1/episode-3.html')#, {'url': url_punch_season1_ep_1()[2]['episode3']['res1080']})


def opm4_1(request):
    return render(request, 'main/onepunchman/season-1/episode-4.html')#, {'url': url_punch_season1_ep_1()[3]['episode4']['res1080']})   


def opm5_1(request):
    return render(request, 'main/onepunchman/season-1/episode-5.html')#, {'url': url_punch_season1_ep_1()[4]['episode5']['res1080']})


def opm6_1(request):
    return render(request, 'main/onepunchman/season-1/episode-6.html')#, {'url': url_punch_season1_ep_1()[5]['episode6']['res1080']})       


def opm7_1(request):
    return render(request, 'main/onepunchman/season-1/episode-7.html')#, {'url': url_punch_season1_ep_1()[6]['episode7']['res1080']})


def opm8_1(request):
    return render(request, 'main/onepunchman/season-1/episode-8.html')#, {'url': url_punch_season1_ep_1()[7]['episode8']['res1080']})


def opm9_1(request):
    return render(request, 'main/onepunchman/season-1/episode-9.html')#, {'url': url_punch_season1_ep_1()[8]['episode9']['res1080']}) 


def opm10_1(request):
    return render(request, 'main/onepunchman/season-1/episode-10.html')#, {'url': url_punch_season1_ep_1()[9]['episode10']['res1080']})


def opm11_1(request):
    return render(request, 'main/onepunchman/season-1/episode-11.html')#, {'url': url_punch_season1_ep_1()[10]['episode11']['res1080']}) 


def opm12_1(request):
    return render(request, 'main/onepunchman/season-1/episode-12.html')#, {'url': url_punch_season1_ep_1()[11]['episode12']['res1080']})        





#onepucnhman 2 season                               
def opm1_2(request):
    return render(request, 'main/onepunchman/season-2/episode-1.html')#, {'url': url_punch_season2_ep_1()[0]['episode1']['res1080']})


def opm2_2(request):
    return render(request, 'main/onepunchman/season-2/episode-2.html')#, {'url': url_punch_season2_ep_1()[1]['episode2']['res1080']})    


def opm3_2(request):
    return render(request, 'main/onepunchman/season-2/episode-3.html')#, {'url': url_punch_season2_ep_1()[2]['episode3']['res1080']})


def opm4_2(request):
    return render(request, 'main/onepunchman/season-2/episode-4.html')#, {'url': url_punch_season2_ep_1()[3]['episode4']['res1080']})   


def opm5_2(request):
    return render(request, 'main/onepunchman/season-2/episode-5.html')#, {'url': url_punch_season2_ep_1()[4]['episode5']['res1080']})


def opm6_2(request):
    return render(request, 'main/onepunchman/season-2/episode-6.html')#, {'url': url_punch_season2_ep_1()[5]['episode6']['res1080']})       


def opm7_2(request):
    return render(request, 'main/onepunchman/season-2/episode-7.html')#, {'url': url_punch_season2_ep_1()[6]['episode7']['res1080']})


def opm8_2(request):
    return render(request, 'main/onepunchman/season-2/episode-8.html')#, {'url': url_punch_season2_ep_1()[7]['episode8']['res1080']})


def opm9_2(request):
    return render(request, 'main/onepunchman/season-2/episode-9.html')#, {'url': url_punch_season2_ep_1()[8]['episode9']['res1080']}) 


def opm10_2(request):
    return render(request, 'main/onepunchman/season-2/episode-10.html')#, {'url': url_punch_season2_ep_1()[9]['episode10']['res1080']})


def opm11_2(request):
    return render(request, 'main/onepunchman/season-2/episode-11.html')#, {'url': url_punch_season2_ep_1()[10]['episode11']['res1080']}) 


def opm12_2(request):
    return render(request, 'main/onepunchman/season-2/episode-12.html')#, {'url': url_punch_season2_ep_1()[11]['episode12']['res1080']})  





#homeless god season 1
def hg1_1(request):
    return render(request, 'main/homeless_god/season-1/episode-1.html')#, {'url': url_noragami_season1_ep_1()[0]['episode1']['res1080']})


def hg2_1(request):
    return render(request, 'main/homeless_god/season-1/episode-2.html')#, {'url': url_noragami_season1_ep_1()[1]['episode2']['res1080']})    


def hg3_1(request):
    return render(request, 'main/homeless_god/season-1/episode-3.html')#, {'url': url_noragami_season1_ep_1()[2]['episode3']['res1080']})


def hg4_1(request):
    return render(request, 'main/homeless_god/season-1/episode-4.html')#, {'url': url_noragami_season1_ep_1()[3]['episode4']['res1080']})


def hg5_1(request):
    return render(request, 'main/homeless_god/season-1/episode-5.html')#, {'url': url_noragami_season1_ep_1()[4]['episode5']['res1080']})


def hg6_1(request):
    return render(request, 'main/homeless_god/season-1/episode-6.html')#, {'url': url_noragami_season1_ep_1()[5]['episode6']['res1080']})


def hg7_1(request):
    return render(request, 'main/homeless_god/season-1/episode-7.html')#, {'url': url_noragami_season1_ep_1()[6]['episode7']['res1080']})


def hg8_1(request):
    return render(request, 'main/homeless_god/season-1/episode-8.html')#, {'url': url_noragami_season1_ep_1()[7]['episode8']['res1080']})


def hg9_1(request):
    return render(request, 'main/homeless_god/season-1/episode-9.html')#, {'url': url_noragami_season1_ep_1()[8]['episode9']['res1080']})


def hg10_1(request):
    return render(request, 'main/homeless_god/season-1/episode-10.html')#, {'url': url_noragami_season1_ep_1()[9]['episode10']['res1080']})


def hg11_1(request):
    return render(request, 'main/homeless_god/season-1/episode-11.html')#, {'url': url_noragami_season1_ep_1()[10]['episode11']['res1080']})


def hg12_1(request):
    return render(request, 'main/homeless_god/season-1/episode-12.html')#, {'url': url_noragami_season1_ep_1()[11]['episode12']['res1080']})





#homeless god season 2
def hg1_2(request):
    return render(request, 'main/homeless_god/season-2/episode-1.html')#, {'url': url_noragami_season2_ep_1()[0]['episode1']['res1080']})


def hg2_2(request):
    return render(request, 'main/homeless_god/season-2/episode-2.html')#, {'url': url_noragami_season2_ep_1()[1]['episode2']['res1080']})    


def hg3_2(request):
    return render(request, 'main/homeless_god/season-2/episode-3.html')#, {'url': url_noragami_season2_ep_1()[2]['episode3']['res1080']})


def hg4_2(request):
    return render(request, 'main/homeless_god/season-2/episode-4.html')#, {'url': url_noragami_season2_ep_1()[3]['episode4']['res1080']})


def hg5_2(request):
    return render(request, 'main/homeless_god/season-2/episode-5.html')#, {'url': url_noragami_season2_ep_1()[4]['episode5']['res1080']})


def hg6_2(request):
    return render(request, 'main/homeless_god/season-2/episode-6.html')#, {'url': url_noragami_season2_ep_1()[5]['episode6']['res1080']})


def hg7_2(request):
    return render(request, 'main/homeless_god/season-2/episode-7.html')#, {'url': url_noragami_season2_ep_1()[6]['episode7']['res1080']})


def hg8_2(request):
    return render(request, 'main/homeless_god/season-2/episode-8.html')#, {'url': url_noragami_season2_ep_1()[7]['episode8']['res1080']})


def hg9_2(request):
    return render(request, 'main/homeless_god/season-2/episode-9.html')#, {'url': url_noragami_season2_ep_1()[8]['episode9']['res1080']})


def hg10_2(request):
    return render(request, 'main/homeless_god/season-2/episode-10.html')#, {'url': url_noragami_season2_ep_1()[9]['episode10']['res1080']})


def hg11_2(request):
    return render(request, 'main/homeless_god/season-2/episode-11.html')#, {'url': url_noragami_season2_ep_1()[10]['episode11']['res1080']})


def hg12_2(request):
    return render(request, 'main/homeless_god/season-2/episode-12.html')#, {'url': url_noragami_season2_ep_1()[11]['episode12']['res1080']})


def hg13_2(request):
    return render(request, 'main/homeless_god/season-2/episode-13.html')#, {'url': url_noragami_season2_ep_1()[12]['episode13']['res1080']})





# dororo 
def dor1(request):
    return render(request, 'main/dororo/episode-1.html')#, {'url': url_dororo_ep_1()[0]['episode1']['res1080']})


def dor2(request):
    return render(request, 'main/dororo/episode-2.html')#, {'url': url_dororo_ep_1()[1]['episode2']['res1080']})


def dor3(request):
    return render(request, 'main/dororo/episode-3.html')#, {'url': url_dororo_ep_1()[2]['episode3']['res1080']})


def dor4(request):
    return render(request, 'main/dororo/episode-4.html')#, {'url': url_dororo_ep_1()[3]['episode4']['res1080']})


def dor5(request):
    return render(request, 'main/dororo/episode-5.html')#, {'url': url_dororo_ep_1()[4]['episode5']['res1080']})


def dor6(request):
    return render(request, 'main/dororo/episode-6.html')#, {'url': url_dororo_ep_1()[5]['episode6']['res1080']})


def dor7(request):
    return render(request, 'main/dororo/episode-7.html')#, {'url': url_dororo_ep_1()[6]['episode7']['res1080']})


def dor8(request):
    return render(request, 'main/dororo/episode-8.html')#, {'url': url_dororo_ep_1()[7]['episode8']['res1080']})


def dor9(request):
    return render(request, 'main/dororo/episode-9.html')#, {'url': url_dororo_ep_1()[8]['episode9']['res1080']})


def dor10(request):
    return render(request, 'main/dororo/episode-10.html')#, {'url': url_dororo_ep_1()[9]['episode10']['res1080']})


def dor11(request):
    return render(request, 'main/dororo/episode-11.html')#, {'url': url_dororo_ep_1()[10]['episode11']['res1080']})


def dor12(request):
    return render(request, 'main/dororo/episode-12.html')#, {'url': url_dororo_ep_1()[11]['episode12]['res1080']})


def dor13(request):
    return render(request, 'main/dororo/episode-13.html')#, {'url': url_dororo_ep_1()[12]['episode13']['res1080']})


def dor14(request):
    return render(request, 'main/dororo/episode-14.html')#, {'url': url_dororo_ep_1()[13]['episode14']['res1080']})


def dor15(request):
    return render(request, 'main/dororo/episode-15.html')#, {'url': url_dororo_ep_1()[14]['episode15']['res1080']})


def dor16(request):
    return render(request, 'main/dororo/episode-16.html')#, {'url': url_dororo_ep_1()[15]['episode16']['res1080']})


def dor17(request):
    return render(request, 'main/dororo/episode-17.html')#, {'url': url_dororo_ep_1()[16]['episode17']['res1080']})


def dor18(request):
    return render(request, 'main/dororo/episode-18.html')#, {'url': url_dororo_ep_1()[17]['episode18']['res1080']})


def dor19(request):
    return render(request, 'main/dororo/episode-19.html')#, {'url': url_dororo_ep_1()[18]['episode19']['res1080']})


def dor20(request):
    return render(request, 'main/dororo/episode-20.html')#, {'url': url_dororo_ep_1()[19]['episode20']['res1080']})


def dor21(request):
    return render(request, 'main/dororo/episode-21.html')#, {'url': url_dororo_ep_1()[20]['episode21']['res1080']})


def dor22(request):
    return render(request, 'main/dororo/episode-22.html')#, {'url': url_dororo_ep_1()[21]['episode22']['res1080']})


def dor23(request):
    return render(request, 'main/dororo/episode-23.html')#, {'url': url_dororo_ep_1()[22]['episode23']['res1080']})


def dor24(request):
    return render(request, 'main/dororo/episode-24.html')#, {'url': url_dororo_ep_1()[23]['episode24']['res1080']})




#tower of  god
def tog1(request):
    return render(request, 'main/tower_of_god/episode-1.html')#, {'url': url_tower_of_god_ep_1()[0]['episode1']['res1080']})    


def tog2(request):
    return render(request, 'main/tower_of_god/episode-2.html')#, {'url': url_tower_of_god_ep_1()[1]['episode2']['res1080']})


def tog3(request):
    return render(request, 'main/tower_of_god/episode-3.html')#, {'url': url_tower_of_god_ep_1()[2]['episode3']['res1080']})


def tog4(request):
    return render(request, 'main/tower_of_god/episode-4.html')#, {'url': url_tower_of_god_ep_1()[3]['episode4']['res1080']})


def tog5(request):
    return render(request, 'main/tower_of_god/episode-5.html')#, {'url': url_tower_of_god_ep_1()[4]['episode5']['res1080']})


def tog6(request):
    return render(request, 'main/tower_of_god/episode-6.html')#, {'url': url_tower_of_god_ep_1()[5]['episode6']['res1080']})


def tog7(request):
    return render(request, 'main/tower_of_god/episode-7.html')#, {'url': url_tower_of_god_ep_1()[6]['episode7']['res1080']})


def tog8(request):
    return render(request, 'main/tower_of_god/episode-8.html')#, {'url': url_tower_of_god_ep_1()[7]['episode8']['res1080']})


def tog9(request):
    return render(request, 'main/tower_of_god/episode-9.html')#, {'url': url_tower_of_god_ep_1()[8]['episode9']['res1080']})


def tog10(request):
    return render(request, 'main/tower_of_god/episode-10.html')#, {'url': url_tower_of_god_ep_1()[9]['episode10']['res1080']})


def tog11(request):
    return render(request, 'main/tower_of_god/episode-11.html')#, {'url': url_tower_of_god_ep_1()[10]['episode11']['res1080']})


def tog12(request):
    return render(request, 'main/tower_of_god/episode-12.html')#, {'url': url_tower_of_god_ep_1()[11]['episode12']['res1080']})


def tog13(request):
    return render(request, 'main/tower_of_god/episode-13.html')#, {'url': url_tower_of_god_ep_1()[12]['episode13']['res1080']})





#tokyo avengers
def ta1(request):
    return render(request, 'main/tokyo_avengers/episode-1.html')#, {'url': url_tokyo_avengers_ep_1()[0]['episode1']['res1080']})


def ta2(request):
    return render(request, 'main/tokyo_avengers/episode-2.html')#, {'url': url_tokyo_avengers_ep_1()[1]['episode2']['res1080']})


def ta3(request):
    return render(request, 'main/tokyo_avengers/episode-3.html')#, {'url': url_tokyo_avengers_ep_1()[2]['episode3']['res1080']})


def ta4(request):
    return render(request, 'main/tokyo_avengers/episode-4.html')#, {'url': url_tokyo_avengers_ep_1()[3]['episode4']['res1080']})


def ta5(request):
    return render(request, 'main/tokyo_avengers/episode-5.html')#, {'url': url_tokyo_avengers_ep_1()[4]['episode5']['res1080']})


def ta6(request):
    return render(request, 'main/tokyo_avengers/episode-6.html')#, {'url': url_tokyo_avengers_ep_1()[5]['episode6']['res1080']})


def ta7(request):
    return render(request, 'main/tokyo_avengers/episode-7.html')#, {'url': url_tokyo_avengers_ep_1()[6]['episode7']['res1080']})


def ta8(request):
    return render(request, 'main/tokyo_avengers/episode-8.html')#, {'url': url_tokyo_avengers_ep_1()[7]['episode8']['res1080']})


def ta9(request):
    return render(request, 'main/tokyo_avengers/episode-9.html')#, {'url': url_tokyo_avengers_ep_1()[8]['episode9']['res1080']})


def ta10(request):
    return render(request, 'main/tokyo_avengers/episode-10.html')#, {'url': url_tokyo_avengers_ep_1()[9]['episode10']['res1080']})


def ta11(request):
    return render(request, 'main/tokyo_avengers/episode-11.html')#, {'url': url_tokyo_avengers_ep_1()[10]['episode11']['res1080']})


def ta12(request):
    return render(request, 'main/tokyo_avengers/episode-12.html')#, {'url': url_tokyo_avengers_ep_1()[11]['episode12']['res1080']})


def ta13(request):
    return render(request, 'main/tokyo_avengers/episode-13.html')#, {'url': url_tokyo_avengers_ep_1()[12]['episode13']['res1080']})


def ta14(request):
    return render(request, 'main/tokyo_avengers/episode-14.html')#, {'url': url_tokyo_avengers_ep_1()[13]['episode14']['res1080']})


def ta15(request):
    return render(request, 'main/tokyo_avengers/episode-15.html')#, {'url': url_tokyo_avengers_ep_1()[14]['episode15']['res1080']})


def ta16(request):
    return render(request, 'main/tokyo_avengers/episode-16.html')#, {'url': url_tokyo_avengers_ep_1()[15]['episode16']['res1080']})


def ta17(request):
    return render(request, 'main/tokyo_avengers/episode-17.html')#, {'url': url_tokyo_avengers_ep_1()[16]['episode17']['res1080']})


def ta18(request):
    return render(request, 'main/tokyo_avengers/episode-18.html')#, {'url': url_tokyo_avengers_ep_1()[17]['episode18']['res1080']})


def ta19(request):
    return render(request, 'main/tokyo_avengers/episode-19.html')#, {'url': url_tokyo_avengers_ep_1()[18]['episode19']['res1080']})


def ta20(request):
    return render(request, 'main/tokyo_avengers/episode-20.html')#, {'url': url_tokyo_avengers_ep_1()[19]['episode20']['res1080']})


def ta21(request):
    return render(request, 'main/tokyo_avengers/episode-21.html')#, {'url': url_tokyo_avengers_ep_1()[20]['episode21']['res1080']})


def ta22(request):
    return render(request, 'main/tokyo_avengers/episode-22.html')#, {'url': url_tokyo_avengers_ep_1()[21]['episode22']['res1080']})


def ta23(request):
    return render(request, 'main/tokyo_avengers/episode-23.html')#, {'url': url_tokyo_avengers_ep_1()[22]['episode23']['res1080']})


def ta24(request):
    return render(request, 'main/tokyo_avengers/episode-24.html')#, {'url': url_tokyo_avengers_ep_1()[23]['episode24']['res1080']})




'''
def user_agent():
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36', 
    'accept': '*/*'
}
    url = 'https://browser-info.ru/'
    r = requests.get(url, headers=HEADERS)
    soup = bs(r.content, 'html.parser')
    block = soup.find('div', id = 'tool_padding')
    check_user = block.find('div', id = 'user_agent').text
    
    return  check_user[12:]
'''




#parser onepunchman season 1
'''
def url_punch_season1_ep_1():
   
    r_ = requests.get('http://127.0.0.1:8000/', params=None)
    #usrag = my_view(r_)
   # r_ = requests.get('http://127.0.0.1:8000/', params=None)
    soup_ = bs(r_.content, 'html.parser')
    items_ = soup_.find('div', id='ghghjjj').text
    #print(items_)
    
#'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    
    
    usr_ag = str(request.user_agent.browser)
    fusr = usr_ag[usr_ag.rfind('=') + 1:usr_ag.rfind(')')]
    fusr1 = fusr[1:-1] + '.127'

    fusr2 = fusr1
    
    
    #f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{fusr1} Safari/537.36'
    
    #HEADERS = {'user-agent': items_, 
   # 'accept': '*/*'
    #}
    
    HEADERS = {'user-agent': usr, 
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
    
#parser onepunchman season 2
def url_punch_season2_ep_1():
    
    #r_ = requests.get('http://127.0.0.1:8000/', params=None)
    #soup_ = bs(r_.content, 'html.parser')
    #items_ = soup_.findAll('div', id='ghghjjj')
    #print(items_)
    

    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36', 
    'accept': '*/*'
    }
    page = 1
    counter = 1
    series = []
    urls = []
    season = 1
    while counter < 13:
        URL = f'https://jut.su/one-punchman/season-2/episode-{page}.html'
    
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

#parser homeless god season 1
def url_noragami_season1_ep_1():
    
   # r_ = requests.get('http://127.0.0.1:8000/', params=None)
    #soup_ = bs(r_.content, 'html.parser')
    #items_ = soup_.findAll('div', id='ghghjjj')
    #print(items_)
    
    

    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36', 
    'accept': '*/*'
    }
    page = 1
    counter = 1
    series = []
    urls = []
    season = 1
    while counter < 13:
        URL = f'https://jut.su/nora-gami/season-1/episode-{page}.html'
    
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




#parser homeless god season 2
def url_noragami_season2_ep_1():
    
   # r_ = requests.get('http://127.0.0.1:8000/', params=None)
    #soup_ = bs(r_.content, 'html.parser')
    #items_ = soup_.findAll('div', id='ghghjjj')
    #print(items_)
    
    

    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36', 
    'accept': '*/*'
    }
    page = 1
    counter = 1
    series = []
    urls = []
    season = 1
    while counter < 14:
        URL = f'https://jut.su/nora-gami/season-2/episode-{page}.html'
    
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





#parser dororo
def url_dororo_ep_1():
    
   # r_ = requests.get('http://127.0.0.1:8000/', params=None)
    #soup_ = bs(r_.content, 'html.parser')
    #items_ = soup_.findAll('div', id='ghghjjj')
    #print(items_)
    
    

    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36', 
    'accept': '*/*'
    }
    page = 1
    counter = 1
    series = []
    urls = []
    season = 1
    while counter < 25:
        URL = f'https://jut.su/dororo/episode-{page}.html'
    
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





#parser tower of god
def url_tower_of_god_ep_1():
    
   # r_ = requests.get('http://127.0.0.1:8000/', params=None)
    #soup_ = bs(r_.content, 'html.parser')
    #items_ = soup_.findAll('div', id='ghghjjj')
    #print(items_)
    
    

    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36', 
    'accept': '*/*'
    }
    page = 1
    counter = 1
    series = []
    urls = []
    season = 1
    while counter < 14:
        URL = f'https://jut.su/kami-tou/episode-{page}.html'
    
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





#parser tokyo avengers
def url_tokyo_avengers_ep_1():
    
   # r_ = requests.get('http://127.0.0.1:8000/', params=None)
    #soup_ = bs(r_.content, 'html.parser')
    #items_ = soup_.findAll('div', id='ghghjjj')
    #print(items_)
    
    

    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36', 
    'accept': '*/*'
    }
    page = 1
    counter = 1
    series = []
    urls = []
    season = 1
    while counter < 14:
        URL = f'https://jut.su/tokyo-revengers/episode-{page}.html'
    
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
    '''