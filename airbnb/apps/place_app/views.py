# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect


def show_place(request):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')
    return render(request, "place/show_place.html")


def new_page(request):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')
    return render(request, "base/new.html")
