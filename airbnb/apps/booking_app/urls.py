from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^(?P<place_id>\d+)/confirm$', views.confirm_pay, name="confirm"),
    url(r'^(?P<place_id>\d+)/create$', views.create_booking, name="create"),
    url(r'^(?P<booking_id>\d+)/success$', views.booking_success, name="success"),
    url(r'^edit$', views.booking_edit_page, name="edit_page"),
    url(r'^update$', views.booking_update, name="update"),
    url(r'^(?P<booking_id>\d+)/cancel$', views.booking_cancel_page, name="cancel"),
    url(r'^(?P<booking_id>\d+)/destroy$', views.booking_destroy, name="destroy"),
    url(r'^view/my_trips$',
        views.booking_view_user_trips, name="view_user_trips"),
    url(r'^(?P<booking_id>\d+)/show$',
        views.booking_show_single_trip, name="view_single_trip"),
    url(r'^view/host/(?P<place_id>\d+)/guests$',
        views.show_host_place_all_guests, name="show_place_guests"),
]
