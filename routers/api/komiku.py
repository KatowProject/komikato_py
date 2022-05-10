import json
import controllers.komiku as komiku
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse(json.dumps(komiku.index(request)), content_type="application/json")

def home(request):
    return HttpResponse(json.dumps(komiku.home(request)), content_type="application/json")

def komik(request, endpoint):
    return HttpResponse(json.dumps(komiku.komik(request, endpoint)), content_type="application/json")

def chapter(request, endpoint):
    return HttpResponse(json.dumps(komiku.chapter(request, endpoint)), content_type="application/json")

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('komik/<str:endpoint>/', komik, name='komik'),
    path('chapter/<str:endpoint>/', chapter, name='chapter'),
]

