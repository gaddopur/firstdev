from django.conf.urls import url
from .import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name = "articles_list"),
    url(r'^create/$', views.article_create, name = "create"),
    url(r'^comment/$', views.postcomment, name = "comment"),
    url(r'^update/(?P<slug>[\w-]+)/$', views.article_update, name = "update"),
    url(r'^delete/(?P<slug>[\w-]+)/$', views.article_delete, name = "delete"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_details, name = "details"),   
]
