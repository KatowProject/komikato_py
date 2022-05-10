import json
import controllers.otakudesu as otakudesu
from django.urls import path    
from django.http import HttpResponse

def index(request):
    return HttpResponse(json.dumps(otakudesu.index(request)), content_type="application/json")

def home(request):
    return HttpResponse(json.dumps(otakudesu.home(request)), content_type="application/json")

def search(request, query):
    return HttpResponse(json.dumps(otakudesu.search(request, query)), content_type="application/json")

def detail(request, endpoint):
    return HttpResponse(json.dumps(otakudesu.detail(request, endpoint)), content_type="application/json")

def eps(request, endpoint):
    return HttpResponse(json.dumps(otakudesu.eps(request, endpoint)), content_type="application/json")

def jadwal_rilis(request):
    return HttpResponse(json.dumps(otakudesu.jadwal_rilis(request)), content_type="application/json")

def daftar_anime(request):
    return HttpResponse(json.dumps(otakudesu.daftar_anime(request)), content_type="application/json")

def complete_anime(request, page=1):
    return HttpResponse(json.dumps(otakudesu.complete_anime(request, page)), content_type="application/json")
urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('search/<str:query>/', search, name='search'),
    path('anime/<str:endpoint>/', detail, name='detail'),
    path('eps/<str:endpoint>/', eps, name='eps'),
    path('jadwal-rilis/', jadwal_rilis, name='jadwal_rilis'),
    path('daftar-anime/', daftar_anime, name='daftar_anime'),
    path('complete-anime/', complete_anime, name='complete_anime'),
    path('complete-anime/page/<int:page>/', complete_anime, name='complete_anime'),
]