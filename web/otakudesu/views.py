import controllers.otakudesu as otakudesu
from django.shortcuts import render

# Create your views here.
def index(request):
    mangas = otakudesu.home(request)
    return render(request, 'otakudesu/index.html', context=mangas)

def search(request, query):
    search = otakudesu.search(request, query)
    return render(request, 'otakudesu/search.html', context=search)

def eps(request, endpoint):
    komik = otakudesu.eps(request, endpoint)
    return render(request, 'otakudesu/eps.html', context=komik)