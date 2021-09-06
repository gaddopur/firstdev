from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^search/$', views.search),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', views.home, name="home"),
]

# if settings.DEBUG:
    # print('hello')
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#     thing = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # print("this the start of first print", thing, type(thing[0])
    # print("this is the start of second print", thing[0].pattern)
    # print("this is third print", dir(thing[0]))
# print(urlpatterns[1], type(ulrpatterns[1]))
