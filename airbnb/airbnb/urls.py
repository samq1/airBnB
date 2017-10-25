"""airbnb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('apps.loginregis_app.urls', namespace="login")),
    url(r'^main/', include('apps.main_router.urls', namespace="main")),
    url(r'^users/', include('apps.airbnb_app.urls', namespace="users")),
    url(r'^places/', include('apps.place_app.urls', namespace="places")),
    url(r'^booking/', include('apps.booking_app.urls', namespace="bookings")),
    url(r'^message/', include('apps.messaging_app.urls', namespace="messages")),
    url(r'^review/', include('apps.review_app.urls', namespace="reviews")),
    url(r'^$', include('apps.main_router.urls', namespace="return_home")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)