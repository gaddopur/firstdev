from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name = 'signup'),
    url(r'^login/$', views.login_view, name = 'login'),
    url(r'^logout/$', views.logout_views, name = 'logout'),
    url(r'^recovery/', views.userRecovery, name="userrecovery"),
    url(r'newpassword/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/$', views.userNewpassword, name='newpassword'),
    url(r'^activate/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/$', views.activate, name='activate'),
    url(r'^(?P<email>[\w.@+-]+)/$', views.profile_views, name = 'profile'),
]
