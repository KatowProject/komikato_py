from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:query>/', views.search, name='search'),
    path('eps/<str:endpoint>/', views.eps, name='eps'),
]