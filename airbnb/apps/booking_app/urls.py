from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^create$', views.create_booking, name="create"),
    url(r'^success$', views.booking_success, name="success"),
    url(r'^edit$', views.booking_edit_page, name="edit_page"),
    url(r'^update$', views.booking_update, name="update"),
    url(r'^remove$', views.booking_remove_page, name="remove"),
    url(r'^destroy$', views.booking_destroy, name="destroy"),
    url(r'^view$', views.booking_view_single, name="view_single"),
    url(r'^show_all$', views.booking_show_all_cribs, name="show_all_cribs"),
    url(r'^show_guests$', views.booking_show_all_guests, name="show_all_guests"),
]
