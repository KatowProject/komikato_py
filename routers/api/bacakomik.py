import json 
import controllers.bacakomik as bacakomik
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse(json.dumps(bacakomik.index(request)), content_type="application/json")

def home(request):
    return HttpResponse(json.dumps(bacakomik.home(request)), content_type="application/json")

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
]
