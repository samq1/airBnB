from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^$', views.main_login, name="main_login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^profile/$', views.user_profile, name="user_profile"),
    url(r'^profile/(?P<User_id>\d+)$', views.show, name="show"),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^users/(?P<User_id>\d+)/update$', views.update, name="update"),
    url(r'^edit/(?P<User_id>\d+)$', views.edit, name="edit_profile"),
    url(r'^process/$', views.process, name="process"),
    url(r'^regiser_newuser/$', views.register_page, name="register_page"),
    url(r'^clear/$', views.clear, name="clear")
]
