from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'filter(?:/ordering=(?P<criteria>(.)+))', views.filter_all, name="filter"),
    url(r'^(?P<place_id>\d+)$', views.show_place, name="show"),
    url(r'^does_not_exist$', views.does_not_exist, name="does_not_exist"),
]
