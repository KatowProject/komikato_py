import controllers.komikindo as komikindo
from django.shortcuts import render

# Create your views here.
def index(request):
    mangas = komikindo.home(request)
    return render(request, 'komikindo/index.html', context=mangas)

def search(request, query):
    search = komikindo.search(request, query)
    return render(request, 'komikindo/search.html', context=search)

def chapter(request, endpoint):
    chapter = komikindo.chapter(request, endpoint)
    return render(request, 'komikindo/chapter.html', context=chapter)

def komik(request, type, page):
    komik = komikindo.komik(request, type, page)
    return render(request, 'komikindo/smut.html', context=komik)