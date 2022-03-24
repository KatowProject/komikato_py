import requests as r
from bs4 import BeautifulSoup

req = r.Session()
req.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})

def get(url, options={}):
    response = req.get(url, params=options)
    # get status code
    status = response.status_code
    if (status == 200):
        return response
    else:
        if "komikindo" in url:
            url = url.replace("komikindo.id", "komikindo-id.translate.goog")
            response = req.get(url + "?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id", params=options)
            
            return response
        
        if "otakudesu" in url:
            url = url.replace("otakudesu.live", "otakudesu-.translate.goog")
            response = req.get(url + "?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id", params=options)
            
            return response
        # url_base64 = base64.b64encode(url.encode('utf-8'))
        # response = req.get("https://bypass.kato-rest.us/url/" + url_base64.decode('utf-8'))
        
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