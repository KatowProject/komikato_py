import json
import requests as r
from django.http import HttpResponse
from bs4 import BeautifulSoup
import os
baseURL = "https://komikindo.id/"

def index(request):
    response = r.get(baseURL)
    
    resolve = json.dumps({
        'status': 'success',
        'message': 'Welcome to Komikindo API',
        'statusCode': response.status_code,
    })
    
    return HttpResponse(resolve, content_type="application/json")

def home(request):
    response = r.get(baseURL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    obj = {}
    obj["menu"] = []
    mangas_menu = soup.find(id="menu-second-menu").find_all("li")
    for manga in mangas_menu:
        name = manga.find("a").text
        link = {
            'url': manga.find("a").get("href"),
            'endpoint': manga.find("a").get("href").replace(baseURL, "")
        }
        
        obj["menu"].append({ 'name': name, 'link': link })
        
    obj["body"] = {}
    mangas_menu = soup.find_all("section", {"class": "whites"})
    for manga in mangas_menu:
        if (manga.find(id="informasi")):
            continue
        
        popular = manga.find_all("div", {"class": "mangapopuler"})
        if (len(popular) > 0):
            obj["body"]["popular"] = []
            mangas = manga.find("div", {"class": "mangapopuler"}).find_all("div", {"class": "animepost"})
            for m in mangas:
                name = m.find("a", itemprop="url").get("title")
                thumb = m.find("img").get("src").split("?")[0]
                link = {
                    'url': m.find("a", itemprop="url").get("href"),
                    'endpoint': m.find("a", itemprop="url").get("href").replace(baseURL, "")
                }
                last_upload = m.find("span", {"class": "datech"}).text
                last_chapter = {
                    'name': m.find("div", {"class": "lsch"}).find("a").text,
                    'url': m.find("div", {"class": "lsch"}).find("a").get("href"),
                    'endpoint': m.find("div", {"class": "lsch"}).find("a").get("href").replace(baseURL, "")
                }
                obj["body"]["popular"].append({ 'name': name, 'thumb': thumb, 'link': link, 'last_upload': last_upload, 'last_chapter': last_chapter })
            
            
        latest = manga.find_all("div", {"class": "latestupdate-v2"})
        if (len(latest) > 0):
            obj["body"]["latest"] = []
            mangas = manga.find_all("div", {"class": "animepost"})
            print(len(latest))
            # for m in mangas:
            #     name = m.find("a", itemprop="url").get("title")
            #     thumb = m.find("img").get("src").split("?")[0]
            #     link = {
            #         'url': m.find("a", itemprop="url").get("href"),
            #         'endpoint': m.find("a", itemprop="url").get("href").replace(baseURL, "")
            #     }
            #     obj["body"]["latest"].append({ 'name': name, 'thumb': thumb, 'link': link })
                 
            
    
    return HttpResponse(json.dumps(obj), content_type="application/json")
    