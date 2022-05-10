import json
import controllers.mangabat as mangabat
from django.urls import path    
from django.http import HttpResponse

def index(request):
    return HttpResponse(json.dumps(mangabat.index(request)), content_type="application/json")

def home(request):
    return HttpResponse(json.dumps(mangabat.home(request)), content_type="application/json")

def comic(request, endpoint):
    return HttpResponse(json.dumps(mangabat.comic(request, endpoint)), content_type="application/json")

def chapter(request, endpoint):
    return HttpResponse(json.dumps(mangabat.chapter(request, endpoint)), content_type="application/json")

def search(request, query):
    return HttpResponse(json.dumps(mangabat.search(request, query)), content_type="application/json")

def genres(request, type=None, pagination=1):
    return HttpResponse(json.dumps(mangabat.genres(request, type, pagination)), content_type="application/json")

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('comic/<str:endpoint>/', comic, name='comic'),
    path('chapter/<str:endpoint>/', chapter, name='api_chapter'),
    path('search/<str:query>/', search, name='search'),
    path('genres/', genres, name='genres'),
    path('genres/<str:type>/', genres, name='genres'),
    path('genres/<str:type>/page/<int:pagination>', genres, name='genres'),
]