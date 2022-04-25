from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


service = Service('D:\\programs_python\\zephyrr33.github.io\\parcer_anime_store\\chromedriver\\chromedriver')
browser = webdriver.Chrome(service=service)
URL = 'http://chrome:/version'
browser.get(url=URL)
#time.sleep(6)
browser.refresh()

print(browser.find_element(By.ID, 'ghghjjj'))
time.sleep(6)


browser.quit()

#search_from = browser.find_element_by_tag_name('html')

#browser = webdriver.Chrome()
'''
page = 1
counter = 1
series = []
urls = []
season = 1
URL = f'https://jut.su/one-punchman/season-1/episode-{page}.html'
browser.get(URL)   
    '''
#links = browser.find_element_by_tag_name('div', id='ghghjjj')

#ur = browser.find_elements_by_tag_name('div').text
'''ur = browser.find_elements(By.TAG_NAME, "div")
time.sleep(10)

for i in ur:
    ur1 = i.find_element(By.CSS_SELECTOR, 'ghghjjj')
    print(ur1.text)'''
'''
ur = browser.find_element(By.CLASS_NAME, value='vjs-tech')
#for i in ur:
 #   ur1 = i.find_element(By.TAG_NAME, value='script')

print(ur.text)
time.sleep(7)
browser.quit()'''