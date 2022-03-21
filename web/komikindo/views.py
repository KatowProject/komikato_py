import controllers.komikindo as komikindo
from django.shortcuts import render

# Create your views here.
def index(request):
    mangas = komikindo.home(request)
    return render(request, 'komikindo/index.html', context=mangas)

def chapter(request, endpoint):
    chapter = komikindo.chapter(request, endpoint)
    return render(request, 'komikindo/chapter.html', context=chapter)