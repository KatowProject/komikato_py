import tools
from bs4 import BeautifulSoup
baseURL = "https://m.mangabat.com/"
altURL = "https://readmangabat.com/"

def index(request):
    response = tools.get(baseURL)
    
    return { 'success': True, 'statusCode': response.status_code }

def home(request):
    response = tools.get(f"{baseURL}")
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    main = soup.find(class_="body-site")
    
    obj = {}
    obj["title"] = "Home"
    obj["url"] = request.build_absolute_uri()
    obj["popular"] = []
    popular = main.find(id="owl-slider").find_all(class_="item")
    for manga in popular:
        name = manga.find("a").text
        thumb = manga.find("img").get("src")
        url = manga.find("a").get("href")
        endpoint = url.replace(baseURL, "")
        
        chapter_name = manga.find_all("a")[1].text
        chapter_url = manga.find_all("a")[1].get("href")
        chapter_endpoint = chapter_url.replace(baseURL, "").replace(altURL, "")
        
        obj["popular"].append({
            'name': name,
            'thumb': thumb,
            'url': url,
            'endpoint': endpoint,
            'chapter': {
               'name': chapter_name,
               'url': chapter_url,
               'endpoint': chapter_endpoint
            }
        })
    
    obj["latest"] = []
    latest = main.find_all(class_="content-homepage-item")
    for manga in latest:
        name = manga.find(class_="item-img").get("title")
        thumb = manga.find("img").get("src")
        score = manga.find(class_="item-rate").text
        url = manga.find(class_="item-img").get("href")
        endpoint = url.replace(baseURL, "").replace(altURL, "")
        
        arr_chapter = []
        chapters = manga.find_all(class_="item-chapter")
        for chapter in chapters:
            chapter_name = chapter.find("a").text
            chapter_url = chapter.find("a").get("href")
            chapter_endpoint = chapter_url.replace(baseURL, "").replace(altURL, "")

            arr_chapter.append({ 'name': chapter_name, 'url': chapter_url, 'endpoint': chapter_endpoint })
        
        obj["latest"].append({
            'name': name,
            'thumb': thumb,
            'url': url,
            'endpoint': endpoint,
            'score': '⭐' + score,
            'chapters': arr_chapter
        })
            
    return obj

def comic(request, endpoint):
    response = tools.get(f"{baseURL}{endpoint}")
    soup = BeautifulSoup(response.text, "html.parser")
    
    is404 = soup.find(style="font: 700 22px sans-serif;")
    if is404 is not None and "404" in is404.text:
        response = tools.get(f"https://readmangabat.com/{endpoint}")
        soup = BeautifulSoup(response.text.replace("https://readmangabat.com/", baseURL), "html.parser")
        is404 = soup.find(style="font: 700 22px sans-serif;")
        
        if is404 is not None and "404" in is404.text:
            return { 'success': False, 'statusCode': 404 }
        
    obj = {}
    main = soup.find(class_="body-site")
    
    obj['name'] = main.find(class_="story-info-right").find("h1").text
    obj['thumb'] = main.find(class_="info-image").find("img").get("src")
    obj['alter'] = main.find(class_="variations-tableInfo").find_all("tr")[0].find(class_="table-value").text
    
    obj["authors"] = []
    authors = main.find(class_="variations-tableInfo").find_all("tr")[1].find(class_="table-value").find_all("a")
    for author in authors:
        author_name = author.text
        author_url = author.get("href")
        author_endpoint = author_url.replace(baseURL, "")
        
        obj["authors"].append({ 'name': author_name, 'url': author_url, 'endpoint': author_endpoint })
    obj["status"] = main.find(class_="variations-tableInfo").find_all("tr")[2].find(class_="table-value").text
    
    obj["genres"] = []
    genres = main.find(class_="variations-tableInfo").find_all("tr")[3].find(class_="table-value").find_all("a")
    for genre in genres:
        genre_name = genre.text
        genre_url = genre.get("href")
        genre_endpoint = genre_url.replace(baseURL, "")
        
        obj["genres"].append({ 'name': genre_name, 'url': genre_url, 'endpoint': genre_endpoint })
    
    info_extends = main.find(class_="story-info-right-extent").find_all("p")
    for info in info_extends:
        key = info.find(class_="stre-label").text.split(":")[0].lower().strip().replace(" ", "_")
        value = info.find(class_="stre-value").text
        
        obj[key] = value
    
    main.find(class_="panel-story-info-description").find("h3").decompose()
    obj["synopsis"] = main.find(class_="panel-story-info-description").text.strip()
    
    obj["chapters"] = []
    chapters = main.find(class_="row-content-chapter").find_all("li")
    for chapter in chapters:
        name = chapter.find("a").text
        date = chapter.find(class_="chapter-time text-nowrap").text
        url = chapter.find("a").get("href")
        endpoint = url.replace(baseURL, "").replace(altURL, "")
        
        obj["chapters"].append({ 'name': name, 'date': date, 'url': url, 'endpoint': endpoint })
        
    return obj

def chapter(request, endpoint):
    response = tools.get(f"{baseURL}{endpoint}")
    soup = BeautifulSoup(response.text, "html.parser")
    
    is404 = soup.find(style="font: 700 22px sans-serif;")
    if is404 is not None and "404" in is404.text:
        response = tools.get(f"https://readmangabat.com/{endpoint}")
        soup = BeautifulSoup(response.text, "html.parser")
        is404 = soup.find(style="font: 700 22px sans-serif;")
        
        if is404 is not None and "404" in is404.text:
            return { 'success': False, 'statusCode': 404 }
    
    obj = {}
    
    obj["title"] = soup.find(class_="panel-chapter-info-top").find("h1").text.capitalize()
    obj["thumb"] = soup.find("meta", property="og:image").get("content")
    obj["synopsis"] = soup.find("meta", property="og:description").get("content")
    
    obj["chapters"] = []
    chapters = soup.find(class_="container-chapter-reader").find_all("img")
    for chapter in chapters:
        image = chapter.get("src").replace("https://", "")
        uri = f"https://cdn-mangabat.katowproject.workers.dev/{image}"
        
        obj["chapters"].append(uri)
        
    obj["chapter"] = {}
    chapter_prev = soup.find(class_="navi-change-chapter-btn-prev")
    chapter_next = soup.find(class_="navi-change-chapter-btn-next")
    if chapter_prev is not None:
        obj["chapter"]["prev"] = chapter_prev.get("href").replace(baseURL, "").replace(altURL, "")
    else:
        obj["chapter"]["prev"] = None
        
    if chapter_next is not None:
        obj["chapter"]["next"] = chapter_next.get("href").replace(baseURL, "").replace(altURL, "")
    else:
        obj["chapter"]["next"] = None
        
    
    return obj

def search(request, query):
    page = request.GET.get("page", 1)
    query = query.replace(" ", "_")
    response = tools.get(f"{baseURL}/search/manga/{query}/?page={page}")
    soup = BeautifulSoup(response.text, "html.parser")
    main = soup.find(class_="body-site")
    
    obj = {}
    
    obj["mangas"] = []
    mangas = main.find(class_="panel-list-story").find_all(class_="list-story-item")
    for manga in mangas:
        name = manga.find("a").get("title")
        thumb = manga.find("img").get("src")
        url = manga.find("a").get("href")
        endpoint = url.replace(baseURL, "")
        if "readmangabat.com" in url:
            endpoint = url.replace(altURL, "")
            
        obj["mangas"].append({ 'name': name, 'thumb': thumb, 'url': url, 'endpoint': endpoint })
    
    obj["pagination"] = []
    pagination = main.find(class_="panel-page-number").find_all("a")
    for page in pagination:
        name = page.text
        if "FIRST" in name:
            name = "<< First Page"
        elif "LAST" in name:
            name = "Last Page >>"
        url = page.get("href", None)
        
        endpoint = url
        if url is None:
            endpoint = None
        elif "readmangabat.com" in url:
            endpoint = url.replace(altURL, "").replace("/manga", "")
        elif "m.mangabat.com" in url:
            endpoint = url.replace(baseURL, "").replace("/manga", "")
            
        obj["pagination"].append({ 'name': name, 'url': url, 'endpoint': endpoint })
        
    return obj
    
def genres(request, type, page):
    obj = {}
    if type is None:
        type = ""
    
    response = tools.get(f"{baseURL}{type}/{page}")    
    soup = BeautifulSoup(response.text, "html.parser")
    
    obj["title"] = soup.title.text.split(" - ")[1]
    is404 = soup.find(style="font: 700 22px sans-serif;")
    if is404 is not None and "404" in is404.text:
        response = tools.get(f"https://readmangabat.com/{type}")
        soup = BeautifulSoup(response.text, "html.parser")
        is404 = soup.find(style="font: 700 22px sans-serif;")
        
        if is404 is not None and "404" in is404.text:
            return { 'success': False, 'statusCode': 404 }
        
    obj["genres"] = []
    genres = soup.find(class_="panel-category").find_all("a")
    for genre in genres:
        name = genre.text
        if name == "":
            name = genre.get("title")
        url = genre.get("href")
        if "?" in url:
            continue
        endpoint = url.replace(baseURL, "").replace(altURL, "")
        
        obj["genres"].append({ 'name': name, 'url': url, 'endpoint': endpoint })
        
    
    if type != "":
        obj["mangas"] = []
        mangas = soup.find(class_="panel-list-story").find_all(class_="list-story-item")
        for manga in mangas:
            name = manga.find("a").get("title")
            thumb = manga.find("img").get("src")
            url = manga.find("a").get("href")
            endpoint = url.replace(baseURL, "").replace(altURL, "")
            
            obj["mangas"].append({ 'name': name, 'thumb': thumb, 'url': url, 'endpoint': endpoint })
            
        obj["pagination"] = []
        pagination = soup.find(class_="panel-page-number").find_all("a")
        for page in pagination:
            name = page.text
            if "FIRST" in name:
                name = "<< First Page"
            elif "LAST" in name:
                name = "Last Page >>"
            url = page.get("href", None)
            
            endpoint = url
            if url is None:
                endpoint = None
            else:
                endpoint = url.replace(baseURL, "").replace(altURL, "")
                end_uri = endpoint.split("/")
                endpoint = f"{end_uri[0]}/page/{end_uri[-1]}"
                
            obj["pagination"].append({ 'name': name, 'url': url, 'endpoint': endpoint })
            
    return obj    
    
    
    
    