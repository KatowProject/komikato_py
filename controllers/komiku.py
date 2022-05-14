import tools
from bs4 import BeautifulSoup
baseURL = "https://komiku.id"

def index(request):
    response = tools.get(baseURL)
    
    return { 'status_code': response.status_code, 'message': response.reason }

def home(request):
    response = tools.get(baseURL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    obj = {}
    obj["title"] = soup.title.text
    
    obj["trending"] = []
    trending = soup.find(id="Trending")
    
    first = trending.find(class_="cv").find("a")
    first_thumb = trending.find("style").text.split("url(")[1].split(");")[0].split("?")[0]
    obj["trending"].append({
        'name': first.find("h3").text,
        'url': first.get("href"),
        'endpoint': first.get("href").replace(baseURL, ""),
        'thumb': first_thumb
    })
    mangas = trending.find_all(class_="ls23")
    for manga in mangas:
        url = manga.find(class_="ls23v").find("a").get("href")
        thumb = manga.find(class_="ls23v").find("a").find("img").get("src").split("?")[0]
        chapter_name = manga.find(class_="ls23j").find("h4").text
        chapter_url = manga.find(class_="ls23j").find("a").get("href")
        
        if "lazy.jpg" in thumb:
            thumb = manga.find(class_="ls23v").find("a").find("img").get("data-src").split("?")[0]
            
        obj["trending"].append({
            'name': chapter_name.split("Chapter")[0].strip(),
            'thumb': thumb,
            'url': url,
            'endpoint': url.replace(baseURL, "").replace("/manga", "/komik"),
            'chapter_name': chapter_name.strip(),
            'chapter_url': chapter_url,
            'chapter_endpoint': chapter_url.replace(baseURL, "").replace("/ch", "/chapter")
        })
        
    obj["terbaru"] = []
    terbaru = soup.find_all(id="Terbaru").pop()
    mangas = terbaru.find_all(class_="ls4")
    for manga in mangas:
        name = manga.find(class_="ls4j").find("h4").text.strip()
        thumb = manga.find(class_="ls4v").find("img").get("src").split("?")[0]
        url = manga.find(class_="ls4j").find("a").get("href")
        endpoint = url.replace(baseURL, "").replace("/manga", "/komik")
        
        if "lazy.jpg" in thumb:
            thumb = manga.find(class_="ls4v").find("img").get("data-src").split("?")[0]
            
        obj["terbaru"].append({ 'name': name, 'thumb': thumb, 'url': url, 'endpoint': endpoint })
        
    obj["quick_genre"] = []
    genres = soup.find_all(class_="ls3")
    for genre in genres:
        name = genre.find(class_="ls3p").find("h4").text.strip()
        url = genre.find(class_="ls3p").find("a").get("href")
        
        obj["quick_genre"].append({ 'name': name, 'url': url })
    
    return obj
    
def komik(request, endpoint):
    response = tools.get(f"{baseURL}/manga/{endpoint}")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    obj = {}
    obj["title"] = soup.title.text
    
    obj["name"] = soup.find("header", id="Judul").find("h1").text.strip()
    obj["thumb"] = soup.find(class_="ims").find("img").get("src").split("?")[0]
    information = soup.find(id="Informasi").find("table", class_="inftable").find_all("tr")
    for info in information:
        key = info.find_all("td")[0].text.strip().lower().replace(" ", "_")
        value = info.find_all("td")[1].text.strip()
        
        obj[key] = value
    
    obj["genres"] = []
    genres = soup.find_all("li", class_="genre")
    for genre in genres:
        obj["genres"].append({
            'name': genre.text.strip(),
            'url': genre.find("a").get("href")
        })
        
    obj["chapters"] = []
    chapters = soup.find(id="Daftar_Chapter").find_all("tr")
    for chapter in chapters:
        if chapter.find("td") is None:
            continue
        title = chapter.find("td", class_="judulseries").text.strip()
        url = chapter.find("td").find("a").get("href")
        endpoint = url.replace(baseURL, "").replace("/ch", "/chapter")
        release_date = chapter.find("td", class_="tanggalseries").text.strip()
        
        obj["chapters"].append({
            'title': title,
            'url': url,
            'endpoint': endpoint,
            'release_date': release_date
        })    
    
    obj["new_chap"] = obj["chapters"][-1]
    obj["last_chapter"] = obj["chapters"][0]
    
    return obj

def chapter(request, endpoint):
    response = tools.get(f"{baseURL}/ch/{endpoint}")
    soup = BeautifulSoup(response.text, 'html.parser')  
    
    obj = {}
    obj["title"] = soup.title.text.split(" - ")[0]
    
    chapters = soup.find(id="Baca_Komik").find_all("img")
    obj["chapter_image"] = []
    for chapter in chapters:
        obj["chapter_image"].append({
            'url': chapter.get("src").split("?")[0],
            'alt': chapter.get("alt"),
            'id': chapter.get("id")
        })
    obj["thumb"] = obj["chapter_image"][0]["url"]
    
    obj["pagination"] = []
    pagination = soup.find("div", class_="nxpr").find_all("a")
    for page in pagination:
        obj["pagination"].append({
            'url': page.get("href"),
            'endpoint': page.get("href").replace(baseURL, "").replace("/ch", "/chapter")
        })
    
    return obj
    