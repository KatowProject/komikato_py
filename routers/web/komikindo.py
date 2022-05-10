import controllers.komikindo as komikindo
from django.urls import path
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

urlpatterns = [
    path('', index, name='index'),
    path('chapter/<str:endpoint>/', chapter, name='chapter'),
    path('search/<str:query>/', search, name='search'),
    path('komik/<str:endpoint>/', komik_detail, name='komik_detail'),
    path('daftar-komik/', daftar_komik, name='daftar_komik'),
    path('daftar-komik/page/<int:page>/', daftar_komik, name='daftar_komik'),
    path('manga/', komik, name='manga'),
    path('manga/page/<int:page>/', komik, name='manga'),
    path('manhwa/', komik, name='manhwa'),
    path('manhwa/page/<int:page>/', komik, name='manhwa'),
    path('manhua/', komik, name='manhua'),
    path('manhua/page/<int:page>/', komik, name='manhua'),
    path('smut/', komik, name='smut'),
    path('smut/page/<int:page>/', komik, name='smut'),
]