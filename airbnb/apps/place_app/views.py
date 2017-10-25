# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..loginregis_app.models import *


def show_place(request):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')
    context = {
        "places": Place.objects.all(),
        "users": User.objects.all(),
        "place1": Place.objects.first()
    }
    return render(request, "place/show_place.html", context)


def new_page(request):
    if "user_id" in request.session:
        return redirect('/users/all')
    else:
        return redirect('/users')
    return render(request, "base/new.html")
