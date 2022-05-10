import controllers.komiku as komiku
from django.urls import path
from django.shortcuts import render

def index(request):
    mangas = komiku.home(request)
    return render(request, 'komiku/index.html', context=mangas)

urlpatterns = [
    path('', index, name='index'),
]
