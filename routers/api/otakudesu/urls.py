from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/<str:query>/', views.search, name='search'),
    path('anime/<str:endpoint>/', views.detail, name='detail'),
    path('eps/<str:endpoint>/', views.eps, name='eps'),
    path('jadwal-rilis/', views.jadwal_rilis, name='jadwal_rilis'),
    path('daftar-anime/', views.daftar_anime, name='daftar_anime'),
    path('complete-anime/', views.complete_anime, name='complete_anime'),
    path('complete-anime/page/<int:page>/', views.complete_anime, name='complete_anime'),
]