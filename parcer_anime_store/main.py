import requests
from bs4 import BeautifulSoup as bs

URL = 'https://jut.su/one-piece/episode-1.html'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', 
    'accept': '*/*'
}
HOST = 'https://jut.su'
r = requests.get(URL, headers=HEADERS, params = None)
soup = bs(r.content, 'html.parser')
series = []

items = soup.findAll('div', class_='videoContent')
for item in items:
    for link in item.find_all('source'):
            link1 = link.get('src')
            print(link1)

items = soup.find_all('video', class_='post_media pm_videojs')











