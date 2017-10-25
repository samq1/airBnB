from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^filter/ordering=(?P<ordering>[-_a-zA-Z0-9]+)/city=(?P<city>\w+)/state=(?P<state>[-_a-zA-Z]+)',
        views.filter_all, name="filter_city"),
    url(r'^filter/ordering=(?P<ordering>[-_a-zA-Z0-9]+)/state=(?P<state>[-_a-zA-Z]+)',
        views.filter_all, name="filter_state"),
    url(r'^filter(?:/ordering=(?P<ordering>(.)+))',
        views.filter_all, name="filter_order_only"),
    url(r'^filter/process', views.get_place_filter, name="filter_process"),
    url(r'^(?P<place_id>\d+)$', views.show_place, name="show"),
    url(r'^(?P<place_id>\d+)/edit$', views.edit_place, name="edit"),
    url(r'^does_not_exist$', views.does_not_exist, name="does_not_exist"),
]
