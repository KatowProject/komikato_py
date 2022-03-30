import requests as req
from bs4 import BeautifulSoup
import base64

def get(url, options={}):
    response = req.get(url, params=options)
    # get status code
    status = response.status_code
    if (status == 200):
        return response
    else:
        url_base64 = base64.b64encode(url.encode('utf-8'))
        response = req.get("https://bypass.kato-rest.us/?q=" + url_base64.decode('utf-8'))
        
def get_media_src(url):
    response = get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    
    src = None
    src1 = soup.find("source")
    src2 = data.split("sources: [")
    if (src1):
        src = src1.get("src")
    elif (len(src2) > 1):
        src = src2[1].split("]")[0].split("'file':")[1].split("'")[1]
    return src

def reverse_proxy(url):
    #decode base64
    url = base64.b64decode(url).decode('utf-8')

    #return as video
    response = req.get(url,)
    
    return response