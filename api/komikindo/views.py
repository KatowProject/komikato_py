import controllers.komikindo as komikindo
from django.http import HttpResponse

def index(request):
    return HttpResponse(komikindo.index())

def home(request):
    return HttpResponse(komikindo.home())

def daftar_komik(request, page):
    return HttpResponse(komikindo.daftar_komik(request, page))

def komik_terbaru(request, page):
    return HttpResponse(komikindo.komik_terbaru(request, page))

def komik(request, type, page):
    return HttpResponse(komikindo.komik(request, type, page))

def komik_detail(request, endpoint):
    return HttpResponse(komikindo.komik_detail(request, endpoint))

def chapter(request, endpoint):
    return HttpResponse(komikindo.chapter(request, endpoint))

def search(request, query):
    return HttpResponse(komikindo.search(request, query))