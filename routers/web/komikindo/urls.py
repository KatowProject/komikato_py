from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chapter/<str:endpoint>/', views.chapter, name='chapter'),
    path('search/<str:query>/', views.search, name='search'),
    path('komik/<str:endpoint>/', views.komik_detail, name='komik_detail'),
    path('daftar-komik/', views.daftar_komik, name='daftar_komik'),
    path('daftar-komik/page/<int:page>/', views.daftar_komik, name='daftar_komik'),
    path('manga/', views.komik, name='manga'),
    path('manga/page/<int:page>/', views.komik, name='manga'),
    path('manhwa/', views.komik, name='manhwa'),
    path('manhwa/page/<int:page>/', views.komik, name='manhwa'),
    path('manhua/', views.komik, name='manhua'),
    path('manhua/page/<int:page>/', views.komik, name='manhua'),
    path('smut/', views.komik, name='smut'),
    path('smut/page/<int:page>/', views.komik, name='smut'),
]