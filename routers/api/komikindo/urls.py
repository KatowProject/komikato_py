from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('daftar-komik/page/<int:page>/', views.daftar_komik, name='daftar_komik'),
    path('komik-terbaru/page/<int:page>/', views.komik_terbaru, name='komik_terbaru'),
    path('komikk/<str:types>/page/<int:page>/', views.komik, name='komik'),
    path('komik/<str:endpoint>/', views.komik_detail, name='komik_detail'),
    path('chapter/<str:endpoint>/', views.chapter, name='chapter'),
    path('search/<str:query>/', views.search, name='search'),
]