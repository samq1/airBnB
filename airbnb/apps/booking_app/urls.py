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
    url(r'^view/(?P<user_id>\d+)/trips$',
        views.booking_view_user_trips, name="view_user_trips"),
    url(r'^show_all$', views.booking_show_all_cribs, name="show_all_cribs"),
    url(r'^show_guests$', views.booking_show_all_guests, name="show_all_guests"),
]
