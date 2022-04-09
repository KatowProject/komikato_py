import controllers.otakudesu as otakudesu
from django.shortcuts import render

# Create your views here.
def index(request):
    mangas = otakudesu.home(request)
    return render(request, 'otakudesu2/index.html', context=mangas)

def search(request, query):
    search = otakudesu.search(request, query)
    return render(request, 'otakudesu2/search.html', context=search)

def eps(request, endpoint):
    komik = otakudesu.eps(request, endpoint)
    return render(request, 'otakudesu2/eps.html', context=komik)

def anime(request, endpoint):
    anime = otakudesu.detail(request, endpoint)
    return render(request, 'otakudesu2/anime.html', context=anime)

def jadwal_rilis(request):
    jadwal_rilis = otakudesu.jadwal_rilis(request)
    return render(request, 'otakudesu2/jadwal-rilis.html', context=jadwal_rilis)

def daftar_anime(request):
    anime_list = otakudesu.daftar_anime(request)
    return render(request, 'otakudesu2/anime-list.html', context=anime_list)

def reverse_proxy(request):
    url = request.GET.get('url')
    return otakudesu.reverse_proxy(request, url)

def complete_anime(request, page=1):
    complete_anime = otakudesu.complete_anime(request, page)
    return render(request, 'otakudesu2/complete-anime.html', context=complete_anime)