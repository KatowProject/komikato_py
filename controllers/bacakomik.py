from bs4 import BeautifulSoup
import tools
baseURL = "https://bacakomik.co/"

def index(request):
    response = tools.get(baseURL)
    
    return { 'success': True, 'statusCode': response.status_code }

def home(request):
    response = tools.get(f"{baseURL}")
    soup = BeautifulSoup(response.text, "html")
    
    obj = {}
    obj["title"] = soup.title.text
    
    newest = soup.find_all_next(class_="whites")
    return soup.prettify()
    
            
            
    return obj
    