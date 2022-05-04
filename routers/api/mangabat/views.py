import json
import controllers.mangabat as mangabat
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