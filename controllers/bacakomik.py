from bs4 import BeautifulSoup
import tools
baseURL = "https://bacakomik.co/"

def index(request):
    response = tools.get(baseURL)
    
    return { 'success': True, 'statusCode': response.status_code }

def home(request):
    response = tools.get(f"{baseURL}")
    soup = BeautifulSoup(response.text, "html.parser")
    
    obj = {}
    whites = soup.find_all("section", class_="whites")
    for white in whites:
        if white.get("id", "n") == "informasi":
            continue
        
        key = white.find(class_="widget-title").text.strip().replace(" ", "_").lower()
        print(key)
        if "manga_terbaru" in key:
            obj["newest"] = []
            mangas = white  .find_all(class_="animepost")
            print(len(mangas))
            
            
    return obj
    