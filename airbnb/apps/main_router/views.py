# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect


def route_handler(request):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')
    return render(request, "base/base.html")


def new_page(request):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')
    return render(request, "base/new.html")
