import json
import tools
import urllib
from bs4 import BeautifulSoup
import config as url

baseURL = url.OTAKUDESU_BASEURL
prox = "https://otakudesu-site.translate.goog/"
proxq = "?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id"

def index(request):
    response = tools.get(baseURL)
    
    return { 'success': True, 'statusCode': response.status_code }

def home(request):
    response = tools.get(baseURL)
    data = response.text.replace(prox, baseURL).replace(proxq, "")
    soup = BeautifulSoup(data, "html.parser")
    
    obj = {}
    obj["url"] = request.build_absolute_uri()
    obj["ongoing"] = []
    animes = soup.find(class_="venz").find_all("li")
    for anime in animes:
        obj["ongoing"].append({
            'name': anime.find(class_="jdlflm").text,
            'thumb': anime.find(class_="thumbz").find("img").get("src"),
            'episode_name': anime.find(class_="epz").text.strip(),
            'hari': anime.find(class_="epztipe").text.strip(),
            'release': anime.find(class_="newnime").text.strip(),
            'url': anime.find(class_="thumb").find("a").get("href"),
            'endpoint': anime.find(class_="thumb").find("a").get("href").replace(baseURL, "").replace(prox, "").replace(proxq, "")
        })
    
    obj["complete"] = []
    animes = soup.find(class_="rseries").find_all(class_="venz")[1].find_all("li")
    for anime in animes:
        obj["complete"].append({
            'name': anime.find(class_="jdlflm").text,
            'thumb': anime.find(class_="thumbz").find("img").get("src"),
            'episode_name': anime.find(class_="epz").text.strip(),
            'hari': anime.find(class_="epztipe").text.strip(),
            'release': anime.find(class_="newnime").text.strip(),
            'url': anime.find(class_="thumb").find("a").get("href"),
            'endpoint': anime.find(class_="thumb").find("a").get("href").replace(baseURL, "").replace(prox, "").replace(proxq, "")
        })
        
        
    return obj

def search(request, query):
    response = tools.get(baseURL + "/?s=" + query.replace(" ", "+") + "&post_type=anime")
    data = response.text.replace(prox, baseURL).replace(proxq, "")
    soup = BeautifulSoup(data, "html.parser")
    
    obj = {}
    obj["url"] = request.build_absolute_uri()
    obj["animes"] = []
    animes = soup.find(class_="chivsrc").find_all("li")
    for anime in animes:
        genres = []
        genress = anime.find(class_="set").find_all("a")
        for genre in genress:
            genres.append({
                'name': genre.text,
                'url': genre.get("href")
            })
            
        obj["animes"].append({
            'name': anime.find("h2").find("a").text,
            'thumb': anime.find("img").get("src"),
            'genres': genres,
            'status': anime.find_all(class_="set")[1].text.split(":")[1].strip(),
            'url': anime.find("h2").find("a").get("href"),
            'endpoint': anime.find("h2").find("a").get("href").replace(baseURL, "").replace(prox, "").replace(proxq, "")
        })
        
    return obj

def detail(request, endpoint):
    response = tools.get(baseURL + "anime/" + endpoint)
    data = response.text.replace(prox, baseURL).replace(proxq, "")
    soup = BeautifulSoup(data, "html.parser")
    
    obj = {}
    obj["id"] = soup.find(rel="shortlink").get("href").split("?p=")[1]
    obj["main_title"] = soup.find(class_="jdlrx").find("h1").text.strip()
    obj["thumb"] = soup.find(class_="wp-post-image").get("src")
    obj["url"] = request.build_absolute_uri()
    obj["title"] = soup.find(class_="infozingle").find_all("p")[0].text.split(":")[1].strip()
    obj["japanese"] = soup.find(class_="infozingle").find_all("p")[1].text.split(":")[1].strip()
    obj["skor"] = soup.find(class_="infozingle").find_all("p")[2].text.split(":")[1].strip()
    obj["producer"] = soup.find(class_="infozingle").find_all("p")[3].text.split(":")[1].strip()
    obj["type"] = soup.find(class_="infozingle").find_all("p")[4].text.split(":")[1].strip()
    obj["status"] = soup.find(class_="infozingle").find_all("p")[5].text.split(":")[1].strip()
    obj["episodes"] = soup.find(class_="infozingle").find_all("p")[6].text.split(":")[1].strip()
    obj["duration"] = soup.find(class_="infozingle").find_all("p")[7].text.split(":")[1].strip()
    obj["release_date"] = soup.find(class_="infozingle").find_all("p")[8].text.split(":")[1].strip()
    obj["studio"] = soup.find(class_="infozingle").find_all("p")[9].text.split(":")[1].strip()
    obj["genre"] = soup.find(class_="infozingle").find_all("p")[10].text.split(":")[1].strip()
    
    obj["sinopsis"] = []
    sinop = soup.find(class_="sinopc").find_all("p")
    for sin in sinop:
        obj["sinopsis"].append(sin.text.strip())
        
    obj["eps"] = []
    episodes = soup.find_all(class_="episodelist")
    for episode in episodes:
        type = episode.find(class_="monktit").text
        if "Lengkap" in type:
            tit = episode.find("a")
            if tit == None:
                continue
            else:
                tit = tit.text
            
            obj["eps"].append({
                'type': "Lengkap",
                'title': tit,
                'url': episode.find("a").get("href"),
                'endpoint': episode.find("a").get("href").replace(baseURL, "").replace(prox, "").replace(proxq, "")
            })
        elif "Batch" in type:
            tit = episode.find("a")
            if tit == None:
                continue
            else:
                tit = tit.text
                
            if "[BATCH]" not in tit:
                continue
            obj["eps"].append({
                'type': "Batch",
                'title': episode.find("a").text,
                'url': episode.find("a").get("href"),
                'endpoint': episode.find("a").get("href").replace(baseURL, "").replace(prox, "").replace(proxq, "")
            })
        elif "List" in type:
            temp = []
            eps = None
            list_response = tools.get(f"{baseURL}wp-admin/admin-ajax.php?action=epslist&id={obj['id']}")
            if list_response.text != '0':
                list_soup = BeautifulSoup(list_response.text, "html.parser")
                eps = list_soup.find_all("li")
            else:
                eps = episode.find("ul").find_all("li")    
            
            for ep in eps:
                temp.append({
                    'title': ep.find("a").text.strip(),
                    'url': ep.find("a").get("href"),
                    'endpoint': ep.find("a").get("href").replace(baseURL + "episode/", "")
                })
            
            obj["eps"].append({
                'type': "List",
                'data': temp
            })
            
    return obj

def eps(request, endpoint):
    query = request.GET.get("id", None)
        
    response = tools.get(f"{baseURL}episode/{endpoint}")
    data = response.text.replace(prox, baseURL).replace(proxq, "")
    soup = BeautifulSoup(data, "html.parser")
    
    obj = {}
    
    obj["title"] = soup.find(class_="venutama").find(class_="posttl").text.strip()
    obj["main_title"] = obj["title"].split("Episode")[0].strip()
    obj["thumb"] = soup.find(class_="cukder").find("img").get("src")
    obj["url"] = request.build_absolute_uri()
    obj["eps_list"] = []
    eps = soup.find(id="selectcog").find_all("option")
    for ep in eps:
        url = ep.get("value")
        obj["eps_list"].append({
            'title': ep.text,
            'url': url,
            'endpoint': url.replace(baseURL, "").replace(prox, "").replace(proxq, "")
        })
    
    stream_link = soup.find(id="lightsVideo").find("iframe").get("src")
    if stream_link is None:
        obj["stream_link"] = "-"
    else:
        obj["stream_link"] = stream_link
    
    if query:
        get_script = soup.find_all("script")
        
        script = None
        for script in get_script:
            if 'action:"' in script.text:
                script = script.text
                break
        
        action = script.split('action:"')[2].split('"')[0]
        action1 = script.split('action:"')[1].split('"')[0]
        query_id = tools.decode_base64(query)
        dict_id = json.loads(query_id)
        
        query_response = tools.post(f"{baseURL}wp-admin/admin-ajax.php", data=f"action={action}", options={
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            }
        })
        
        dict_id["action"] = action1
        dict_id["nonce"] = query_response.json()["data"]
        
        _id = urllib.parse.urlencode(dict_id, doseq=False)
        query_response = tools.post(f"{baseURL}wp-admin/admin-ajax.php", data=_id, options={
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
            }
        })
        
        query_data = json.loads(query_response.text)
        print(query_data)
        decode_data = tools.decode_base64(query_data["data"])
        url = decode_data.split('src="')[1].split('"')[0]
        
        obj["stream_link"] = url
                
    obj["mirror_stream_link"] = []
    mrr = soup.find(class_="mirrorstream").find_all("ul")
    for mr in mrr:
        temp = []
        class_ = mr.get("class")[0]
        
        if "480" in class_:
            lis = mr.find_all("li")
            for li in lis:
                url = li.find("a").get("data-content")
                temp.append({
                    'title': li.find("a").text.strip(),
                    'url': url,
                })
                
            obj["mirror_stream_link"].append({
                'name': "480p",
                'data': temp
            })
        elif "720" in class_:
            lis = mr.find_all("li")
            for li in lis:
                url = li.find("a").get("data-content")
                temp.append({
                    'title': li.find("a").text.strip(),
                    'url': url,
                })
                
            obj["mirror_stream_link"].append({
                'name': "720p",
                'data': temp
            })
                
    
    obj["download_link"] = []
    i = 0
    animes = soup.find(class_="download").find_all("li")
    for anime in animes:
        temp = []
        medias = anime.find_all("a")
        for media in medias:
            temp.append({
                'title': media.text.strip(),
                'url': media.get("href"),
            })
        
        obj["download_link"].append({
            'name': anime.find("strong").text.strip(),
            'data': temp,
            'i': f"heading-{i +1}"
        })
        i=i+1
    return obj

def jadwal_rilis(request):
    obj = {}
    obj["title"] = "Jadwal Rilis Anime"
    obj["url"] = request.build_absolute_uri()
    
    res = tools.get(f"{baseURL}/jadwal-rilis")
    data = res.text.replace(prox, baseURL).replace(proxq, "")
    soup = BeautifulSoup(data, "html.parser")
    
    obj["schedule"] = []
    schedules = soup.find_all(class_="kglist321")
    for sch in schedules:
        temp = {}
        temp["day"] = sch.find("h2").text.strip()
        temp["animes"] = []
        
        animes = sch.find_all("li")
        for anime in animes:
            data = {
                'title': anime.find("a").text.strip(),
                'url': anime.find("a").get("href"),
                'endpoint': anime.find("a").get("href").replace(baseURL, "").replace(prox, "").replace(proxq, "")
            }
            temp["animes"].append(data)
        obj["schedule"].append(temp)
            
    return obj

def daftar_anime(request):
    response = tools.get(f"{baseURL}/anime-list")
    data = response.text.replace(prox, baseURL).replace(proxq, "")
    soup = BeautifulSoup(data, "html.parser")
    
    obj = {}
    obj["title"] = "Anime List"
    obj["url"] = request.build_absolute_uri()
    
    obj["anime_list"] = []
    dftkrtn = soup.find(class_="daftarkartun")
    paragraf = dftkrtn.find_all(class_="bariskelom")
    for parag in paragraf:
        name = parag.find(class_="barispenz").find("a").text
        animes = parag.find_all(class_="penzbar")
        
        par = []
        for anime in animes:
            temp = {}
            info = anime.find("a")
            if info == None:
                continue
            temp["title"] = info.get("title")
            temp["url"] = info.get("href")
            temp["endpoint"] = info.get("href").replace(baseURL, "").replace(prox, "").replace(proxq, "")
            
            par.append(temp)
        
        obj["anime_list"].append({
            'name': name,
            'animes': par
        })
            
    return obj

def complete_anime(request, page):
    response = tools.get(f"{baseURL}complete-anime/page/{page}")
    data = response.text.replace(prox, baseURL).replace(proxq, "")
    soup = BeautifulSoup(data, "html.parser")
    main = soup.find(id="venkonten")
    
    obj = {}
    obj["title"] = "Complete Anime"
    obj["url"] = request.build_absolute_uri()
    
    obj["animes"] = []
    animes = main.find(class_="venz").find_all("li")
    for anime in animes:
        name = anime.find(class_="thumbz").find("h2").text
        thumb = anime.find(class_="thumbz").find("img").get("src")
        eps = anime.find(class_="epz").text
        score = anime.find(class_="epztipe").text
        date = anime.find(class_="newnime").text
        url = anime.find(class_="thumb").find("a").get("href")
        endpoint = anime.find(class_="thumb").find("a").get("href").replace(baseURL, "").replace(prox, "").replace(proxq, "")
        
        obj["animes"].append({
            'name': name,
            'thumb': thumb,
            'episode_name': eps,
            'score': score,
            'release': date,
            'url': url,
            'endpoint': endpoint
        })
        
    obj["pagination"] = []
    pagination = main.find(class_="pagination").find_all(class_="page-numbers")
    for page in pagination:
        name = page.text
        url = page.get("href")
        
        endpoint = None
        if url is not None:
            endpoint = url.replace(baseURL, "").replace(prox, "").replace(proxq, "")
        
        obj["pagination"].append({
            'name': name,
            'url': url,
            'endpoint': endpoint
        })
        
        
    return obj

def reverse_proxy(request, url):
    response = tools.reverse_proxy(url)
    
    return response.raw

     
        