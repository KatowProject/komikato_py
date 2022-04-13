from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('daftar-komik/page/<int:page>/', views.daftar_komik, name='api_daftar_komik'),
    path('komik-terbaru/page/<int:page>/', views.komik_terbaru, name='api_komik_terbaru'),
    path('komikk/<str:types>/page/<int:page>/', views.komik, name='api_komik'),
    path('komik/<str:endpoint>/', views.komik_detail, name='api_komik_detail'),
    path('chapter/<str:endpoint>/', views.chapter, name='api_chapter'),
    path('search/<str:query>/', views.search, name='api_search'),
]