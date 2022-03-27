from django.shortcuts import render

def index(request):
    return render(request, 'index2.html', context={})
    