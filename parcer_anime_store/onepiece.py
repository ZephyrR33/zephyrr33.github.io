import requests
from bs4 import BeautifulSoup as bs

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36', 
    'accept': '*/*'
}
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.366
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36

page = 1
counter = 1
series = []
urls = []
season = 1

# теперь это ванпанчмен

#season-1/
#nora-gami
#one-punchman
#jujutsu-kaisen
#dororo
#

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
print(series)


'''
URL = f'https://jut.su/oneepiece/episode-1.html'  
r = requests.get(URL, headers=HEADERS, params = None)
soup = bs(r.content, 'html.parser')
items = soup.findAll('div', class_='videoBlock')
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
print(series)
'''


'''
r_ = requests.get('http://127.0.0.1:8000/', params=None)
soup_ = bs(r_.content, 'html.parser')
items_ = soup_.findAll('div')
print(items_)
'''