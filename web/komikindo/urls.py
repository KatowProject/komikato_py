from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chapter/<str:endpoint>/', views.chapter, name='chapter'),
    path('search/<str:query>/', views.search, name='search'),
    path('komikk/<str:type>/page/<int:page>/', views.komik, name='komik'),
    path('komik/<str:endpoint>/', views.komik_detail, name='komik_detail'),
    path('daftar-komik/', views.daftar_komik, name='daftar_komik'),
    path('daftar-komik/page/<int:page>/', views.daftar_komik, name='daftar_komik'),
]