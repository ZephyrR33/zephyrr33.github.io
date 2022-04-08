from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='D:\\programs_python\\parcer_anime_store\\chromedriver\\chromedriver.exe')
browser.get('https://jut.su/one-piece/episode-1.html')
search_from = browser.find_element_by_tag_name('html')

links = browser.find_element_by_tag_name('div')
for i in links:
    try:
        video_link = i.get('src')
        print(video_link)
    except Exception:
        pass