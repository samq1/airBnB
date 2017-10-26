from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^(?P<User_id>\d+)$', views.review_users, name="review_users"),
    url(r'^review_place/(?P<Place_id>\d+)$', views.review_places, name="review_places"),
    url(r'^(?P<User_id>\d+)/process_user$', views.process_host_user_review, name="process_userreview"),
    url(r'^(?P<Place_id>\d+)/process_placereview/$', views.process_placereview, name="process_placereview"),
]
