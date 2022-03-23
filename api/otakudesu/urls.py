from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/<str:query>/', views.search, name='search'),
    path('anime/<str:endpoint>/', views.detail, name='detail'),
    path('eps/<str:endpoint>/', views.eps, name='eps'),
]