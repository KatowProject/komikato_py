from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('comic/<str:endpoint>/', views.comic, name='comic'),
    path('chapter/<str:endpoint>/', views.chapter, name='api_chapter'),
    path('search/<str:query>/', views.search, name='search'),
    path('genres/', views.genres, name='genres'),
    path('genres/<str:type>/', views.genres, name='genres'),
    path('genres/<str:type>/page/<int:pagination>', views.genres, name='genres'),
]