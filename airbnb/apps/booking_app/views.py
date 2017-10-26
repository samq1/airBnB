# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..loginregis_app.models import *
from datetime import datetime


def create_booking(request):
    return render(request, 'booking/success.html')


def booking_success(request):
    return render(request, 'booking/success.html')


def booking_edit_page(request):
    return render(request, 'booking/success.html')


def booking_update(request):
    return render(request, 'booking/success.html')


def booking_remove_page(request):
    return render(request, 'booking/success.html')


def booking_destroy(request):
    return render(request, 'booking/success.html')


def booking_view_single(request):
    return render(request, 'booking/success.html')


def booking_show_all_cribs(request):
    return render(request, 'booking/success.html')


def booking_show_all_guests(request):
    return render(request, 'booking/success.html')
