from django.conf.urls import url
from .import views

app_name = 'meetings'

urlpatterns = [
    url(r'^requestmeet/$', views.request_meet, name = 'requestmeet'),
    url(r'^listrequestmeet/$', views.list_request_meet, name = 'listrequestmeet'),
    url(r'^acceptmeet/$', views.accept_meet, name = 'acceptmeet'),
    url(r'^donemeet/$', views.done_meet, name = 'donemeet'),
]
