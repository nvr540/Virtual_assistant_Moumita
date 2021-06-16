from os import name
from typing import Mapping
from bs4 import BeautifulSoup
import requests, html5lib, webbrowser
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
    searchGoogle("nivrta podder", 3)

# linkElements = soup.select('.r a')
# print(linkElements)