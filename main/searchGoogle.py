from os import name
from typing import Mapping
from bs4 import BeautifulSoup
import bs4
import requests, html5lib, webbrowser, urllib.request, re
def searchYoutube(searched, numberOfTab):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    url = "https://www.youtube.com/results?search_query=hack"
    webbrowser.open(url)
def searchGoogle(searched, numberOfTab):
    url = f"https://www.google.com/search?q={searched}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    anchor = soup.find_all('a')
    i = 1
    for anc in anchor:
        if "/url" in anc.get("href") :
            print(anc.get("href"))
            webbrowser.open("http://google.com" + str(anc.get("href")))
            i+=1
        if i > numberOfTab:
            break
if __name__ == '__main__':
    searchYoutube("hack", 3)

# linkElements = soup.select('.r a')
# print(linkElements)