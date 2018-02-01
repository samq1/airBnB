# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..loginregis_app.models import *




def route_handler(request):


    return render(request, "base/base.html")


def new_page(request, ordering=None, city=None, state=None):

    places = Place.objects.all()

    if city:
        city = city.replace("_", " ")
        places = places.filter(city=city)
    if state:
        state = state.replace("_", " ")
        places = places.filter(state=state)

    if ordering == "price":
        places = places.order_by('price_night')
    elif ordering == "-price":
        places = places.order_by('-price_night')
    else:
        places = places.order_by('price_night')

    context = {
        "placestoo": Place.objects.filter(state="Texas"),
        "places": places.filter(state="Florida"),
        "locations": Place.objects.order_by(
            'city').values('city', 'state').distinct(),
        "states": Place.objects.order_by('state').values('state').distinct(),
        "Picture": Picture.objects.all().values('image'),
        "place": Place.objects.all(),
    }
    

    return render(request, "base/new.html", context)
