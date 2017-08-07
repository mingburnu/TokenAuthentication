from django.conf.urls import url
from rest_framework.authtoken import views as rest_framework_views
from accounts.views import login_user, logout_user

urlpatterns = [
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
