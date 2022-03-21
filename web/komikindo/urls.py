from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chapter/<str:endpoint>/', views.chapter, name='chapter'),
    path('search/<str:query>/', views.search, name='search'),
    path('komikk/<str:type>/page/<int:page>/', views.komik, name='komik'),
]