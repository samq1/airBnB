from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^new', views.new_page),
    url(r'^', views.route_handler),
]
