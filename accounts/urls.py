from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name = 'signup'),
    url(r'^login/$', views.login_view, name = 'login'),
    url(r'^logout/$', views.logout_views, name = 'logout'),
    url(r'^(?P<username>[\w-]+)/$', views.profile_views, name = 'profile'),
]
