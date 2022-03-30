import controllers.komikindo as komikindo
from django.shortcuts import render

# Create your views here.
def index(request):
    mangas = komikindo.home(request)
    return render(request, 'komikindo2/index.html', context=mangas)

def search(request, query):
    search = komikindo.search(request, query)
    return render(request, 'komikindo2/search.html', context=search)

def chapter(request, endpoint):
    chapter = komikindo.chapter(request, endpoint)
    if chapter == None:
        return render(request, '404.html')
    return render(request, 'komikindo2/chapter.html', context=chapter)

def komik(request, page=1):
    type = request.resolver_match.url_name
    komik = komikindo.komik(request, type, page)
    if komik == None:
        return render(request, '404.html')
    return render(request, 'komikindo2/komikk.html', context=komik)

def komik_detail(request, endpoint):
    komik_detail = komikindo.komik_detail(request, endpoint)
    if komik_detail == None:
        return render(request, '404.html')
    return render(request, 'komikindo2/komik.html', context=komik_detail)

def daftar_komik(request, page=1):
    komik_list = komikindo.daftar_komik(request, page)
    return render(request, 'komikindo2/daftar-komik.html', context=komik_list)