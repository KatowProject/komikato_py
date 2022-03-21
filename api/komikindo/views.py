import json
import controllers.komikindo as komikindo
from django.http import HttpResponse

def index(request):
    return HttpResponse(json.dumps(komikindo.index(request)))

def home(request):
    return HttpResponse(json.dumps(komikindo.home(request)))

def daftar_komik(request, page):
    return HttpResponse(json.dumps(komikindo.daftar_komik(request, page)))

def komik_terbaru(request, page):
    return HttpResponse(json.dumps(komikindo.komik_terbaru(request, page)))

def komik(request, type, page):
    return HttpResponse(json.dumps(komikindo.komik(request, type, page)))

def komik_detail(request, endpoint):
    return HttpResponse(json.dumps(komikindo.komik_detail(request, endpoint)))

def chapter(request, endpoint):
    return HttpResponse(json.dumps(komikindo.chapter(request, endpoint)))

def search(request, query):
    return HttpResponse(json.dumps(komikindo.search(request, query)))