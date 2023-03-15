"""komikato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve

re_pattern = [
    re_path(r"^assets/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT})
]
urlpatterns = [
    path('', views.index, name='index'),
    path('bookmarks/', views.bookmark, name='bookmarks'),
    path('komikindo/', include('routers.web.komikindo')),
    path('otakudesu/', include('routers.web.otakudesu')),
    path('mangabat/', include('routers.web.mangabat')),
    path('komiku/', include('routers.web.komiku')),
    #path('bacakomik/', include('routers.web.bacakomik.urls')),
    path('api/komikindo/', include('routers.api.komikindo')),
    path('api/otakudesu/', include('routers.api.otakudesu')),
    path('api/mangabat/', include('routers.api.mangabat')),
    path('api/bacakomik/', include('routers.api.bacakomik')),
    path('api/komiku/', include('routers.api.komiku')),
    path('', include(re_pattern))
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

handler404 = views.handle_not_found
handler400 = views.handle_bad_request
