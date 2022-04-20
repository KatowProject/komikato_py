import controllers.mangabat as mangabat
from django.shortcuts import render

def index(request):
    mangas = mangabat.home(request)
    return render(request, 'mangabat/index.html', context=mangas)

def comic(request, endpoint):
    return render(request, 'mangabat/comic.html', context=mangabat.comic(request, endpoint))