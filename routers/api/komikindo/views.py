import json
import controllers.komikindo as komikindo
from django.http import HttpResponse

def index(request):
    return HttpResponse(json.dumps(komikindo.index(request)), content_type="application/json")

def home(request):
    return HttpResponse(json.dumps(komikindo.home(request)), content_type="application/json")

def daftar_komik(request, page):
    return HttpResponse(json.dumps(komikindo.daftar_komik(request, page)), content_type="application/json")

def komik_terbaru(request, page):
    return HttpResponse(json.dumps(komikindo.komik_terbaru(request, page)), content_type="application/json")

def komik(request, types, page):
    return HttpResponse(json.dumps(komikindo.komik(request, types, page)), content_type="application/json")

def komik_detail(request, endpoint):
    return HttpResponse(json.dumps(komikindo.komik_detail(request, endpoint)), content_type="application/json")

def chapter(request, endpoint):
    return HttpResponse(json.dumps(komikindo.chapter(request, endpoint)), content_type="application/json")

def search(request, query):
    return HttpResponse(json.dumps(komikindo.search(request, query)), content_type="application/json")