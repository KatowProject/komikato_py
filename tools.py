import requests as r
import base64
import json

req = r.Session()
req.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})

def get(url, options={}):
    response = req.get(url, params=options)
    # get status code
    status = response.status_code
    if (status == 200):
        return response
    else:
        url_base64 = base64.b64encode(url.encode('utf-8'))
        response = req.get("https://bypass.kato-rest.us/url/" + url_base64.decode('utf-8'))
        if (response.status_code == 200 and json.loads(response.text)['status'] == 'error'):
            if "komikindo" in url:
                url = url.replace("komikindo.id", "komikindo-id.translate.goog")
                response = req.get(url + "?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id", params=options)
                return response