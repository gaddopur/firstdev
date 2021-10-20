from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^search/$', views.search),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    path('<str:nouse>/', views.home, name="home")
]
