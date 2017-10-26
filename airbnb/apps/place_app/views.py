# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from ..loginregis_app.models import *
import ast


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
        "place1": place,
        "today": datetime.today().strftime("%Y-%m-%d")
    }
    return render(request, "place/show_place.html", context)


def edit_place(request, place_id):
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
    return render(request, "place/update_place.html", context)


def get_place_filter(request):
    if request.POST['filter_type'] == "city_state":
        filter_dict = ast.literal_eval(request.POST['filter'])
        filter_city = filter_dict['city'].replace(" ", "_")
        filter_state = filter_dict['state'].replace(" ", "_")
        return redirect(reverse('places:filter_city', kwargs={'ordering': "price", 'city': filter_city, 'state': filter_state}))
    else:
        filter_state = request.POST['filter'].replace(" ", "_")
        return redirect(reverse('places:filter_state', kwargs={'ordering': "price", 'state': filter_state}))
    return redirect(reverse('places:filter_order_only', kwargs={'ordering': "price"}))


def filter_all(request, ordering=None, city=None, state=None):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')
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
