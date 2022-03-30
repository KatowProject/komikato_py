import json
import controllers.otakudesu as otakudesu
from django.http import HttpResponse

def index(request):
    return HttpResponse(json.dumps(otakudesu.index(request)))

def home(request):
    return HttpResponse(json.dumps(otakudesu.home(request)))

def search(request, query):
    return HttpResponse(json.dumps(otakudesu.search(request, query)))

def detail(request, endpoint):
    return HttpResponse(json.dumps(otakudesu.detail(request, endpoint)))

def eps(request, endpoint):
    return HttpResponse(json.dumps(otakudesu.eps(request, endpoint)))