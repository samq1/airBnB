from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^', views.new_page),
    url(r'^new', views.route_handler),
]
