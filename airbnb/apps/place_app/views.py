# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from ..loginregis_app.models import *


def show_place(request, place_id):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')
    try:
        place = Place.objects.get(id=place_id)
    except:
        return redirect(reverse('places:does_not_exist'))
    context = {
        "users": User.objects.all(),
        "place1": place
    }
    return render(request, "place/show_place.html", context)


def filter_all(request, criteria):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')

    if criteria == "price":
        places = Place.objects.order_by('price_night')
    elif criteria == "-price":
        places = Place.objects.order_by('-price_night')
    else:
        places = Place.objects.order_by('price_night')

    context = {
        "places": places,
        "locations": Place.objects.order_by(
            'city').values('city', 'state').distinct(),
        "states": Place.objects.order_by('state').values('state').distinct(),
    }
    return render(request, "place/filter_all.html", context)


def does_not_exist(request):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')
    return render(request, "place/does_not_exist.html")


def new_page(request):
    if "user_id" in request.session:
        return redirect('/users/all')
    else:
        return redirect('/users')
    return render(request, "base/new.html")
