import json
import controllers.komikindo as komikindo
from django.urls import path    
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

def genre_list(request):
    return HttpResponse(json.dumps(komikindo.genre_list(request)), content_type="application/json")

def genre(request, genre, page):
    return HttpResponse(json.dumps(komikindo.genre(request, genre, page)), content_type="application/json")

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('daftar-komik/page/<int:page>/', daftar_komik, name='daftar_komik'),
    path('komik-terbaru/page/<int:page>/', komik_terbaru, name='komik_terbaru'),
    path('komikk/<str:types>/page/<int:page>/', komik, name='komik'),
    path('komik/<str:endpoint>/', komik_detail, name='komik_detail'),
    path('chapter/<str:endpoint>/', chapter, name='chapter'),
    path('search/<str:query>/', search, name='search'),
    path('genres/', genre_list, name='genres'),
    path('genres/<str:genre>/page/<int:page>', genre, name='komik'),
]