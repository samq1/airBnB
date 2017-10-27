# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.humanize.templatetags.humanize import intcomma
from django.urls import reverse
from ..loginregis_app.models import *
from datetime import datetime
import json
import decimal


def confirm_pay(request, place_id):
    user_name = User.objects.get(id=request.session['user_id']).first_name
    check_in_date = request.POST['check_in']
    check_in_date = datetime.strptime(check_in_date, '%m/%d/%Y')
    check_in_str = check_in_date.strftime("%m/%d/%Y")
    request.session['check_in'] = check_in_str
    check_out_date = request.POST['check_out']
    check_out_date = datetime.strptime(check_out_date, '%m/%d/%Y')
    check_out_str = check_out_date.strftime("%m/%d/%Y")
    request.session['check_out'] = check_out_str
    num_guests = request.POST['num_guests']
    request.session['num_guests'] = num_guests

    price_night = Place.objects.get(id=place_id).price_night
    num_nights = (check_out_date - check_in_date)
    num_nights = num_nights.days
    int_nights = int(num_nights)
    charge_nights = (decimal.Decimal(
        int_nights) * decimal.Decimal(price_night)).quantize(decimal.Decimal('.01'))
    price_cleaning = Place.objects.get(id=place_id).price_cleaning
    price_servicefee = Place.objects.get(id=place_id).price_servicefee
    price_amenitites = Place.objects.get(id=place_id).price_amenitites

    charge_subtotal = charge_nights + price_cleaning + price_servicefee + price_amenitites
    tax_percent = 0.08
    charge_tax = (decimal.Decimal(charge_subtotal) * decimal.Decimal(tax_percent)).quantize(decimal.Decimal('.01'))
    charge_total = charge_subtotal + charge_tax
    context = {
        'user_name': user_name,
        'place1': Place.objects.get(id=place_id),
        'num_nights': num_nights,
        'charge_nights': charge_nights,
        'charge_subtotal': charge_subtotal,
        'charge_tax': charge_tax,
        'charge_total': charge_total,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'num_guests': request.session['num_guests'],
    }
    return render(request, 'booking/confirm_pay.html', context)


def create_booking(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except:
        return redirect(reverse('places:does_not_exist'))
    guest = User.objects.get(id=request.session['user_id'])
    check_in = datetime.strptime(request.session['check_in'], '%m/%d/%Y')
    check_out = datetime.strptime(request.session['check_out'], '%m/%d/%Y')
    num_guests = request.session['num_guests']

    price_night = place.price_night
    num_nights = (check_out - check_in)
    num_nights = num_nights.days
    int_nights = int(num_nights)
    charge_nights = (decimal.Decimal(
        int_nights) * decimal.Decimal(price_night)).quantize(decimal.Decimal('.01'))
    price_cleaning = place.price_cleaning
    price_servicefee = place.price_servicefee
    price_amenitites = place.price_amenitites
    charge_subtotal = charge_nights + price_cleaning + price_servicefee + price_amenitites

    tax_percent = 0.08
    charge_tax = (decimal.Decimal(charge_subtotal) * decimal.Decimal(tax_percent)).quantize(decimal.Decimal('.01'))

    new_booking = Booking.objects.create(
        place = place,
        guest = guest,
        check_in = check_in,
        check_out = check_out,
        num_guests = num_guests,
        price_night = charge_nights,
        price_cleaning = price_cleaning,
        price_servicefee = price_servicefee,
        price_tax = charge_tax,
        price_amenitites = price_amenitites,
    )
    booking_id = new_booking.id

    return redirect(reverse('bookings:success', kwargs={'booking_id': booking_id}))


def booking_success(request, booking_id):
    user_name = User.objects.get(id=request.session['user_id']).first_name
    booking = Booking.objects.get(id=booking_id)
    charge_total = booking.price_night + booking.price_cleaning + booking.price_servicefee + booking.price_amenitites + booking.price_tax
    guest = User.objects.get(id=request.session['user_id'])

    booking.listed_by.add(guest)
    guest.listed_vacations.add(booking_id)
    booking.save()
    # guest.save()

    context = {
        'user_name': user_name,
        'booking': booking,
        'charge_total': charge_total,
    }
    return render(request, 'booking/success.html', context)


def booking_edit_page(request):
    return render(request, 'booking/success.html')


def booking_update(request):
    return render(request, 'booking/success.html')


def booking_cancel_page(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except:
        return redirect(reverse('booking:view_user_trips'))

    check_in = booking.check_in
    check_out = booking.check_out

    price_night = booking.price_night
    num_nights = (check_out - check_in)
    num_nights = num_nights.days
    int_nights = int(num_nights)
    charge_nights = (decimal.Decimal(
        int_nights) * decimal.Decimal(price_night)).quantize(decimal.Decimal('.01'))
    price_cleaning = booking.price_cleaning
    price_servicefee = booking.price_servicefee
    price_amenitites = booking.price_amenitites
    charge_subtotal = charge_nights + price_cleaning + price_servicefee + price_amenitites
    tax_percent = 0.08
    charge_tax = (decimal.Decimal(charge_subtotal) * decimal.Decimal(tax_percent)).quantize(decimal.Decimal('.01'))
    charge_total = charge_subtotal + charge_tax

    context = {
        'booking': booking,
        'num_nights': num_nights,
        'charge_nights': charge_nights,
        'charge_subtotal': charge_subtotal,
        'charge_tax': charge_tax,
        'charge_total': charge_total,
    }
    return render(request, 'booking/confirm_cancel.html', context)


def booking_destroy(request, booking_id):
    cancel_booking = Booking.objects.get(id=booking_id)
    cancel_booking.is_cancel = True
    cancel_booking.save()
    return redirect('/booking/view/my_trips')


def booking_view_user_trips(request):
    user_name = User.objects.get(id=request.session['user_id']).first_name
    today = datetime.now()
    user_bookings = Booking.objects.filter(
        guest=request.session['user_id']).order_by('check_in')
    context = {
        'user_name': user_name,
        'user_bookings': user_bookings,
        'today': today,
    }
    return render(request, 'booking/view_user_trips.html', context)


def booking_show_single_trip(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except:
        return redirect(reverse('booking:view_user_trips'))
    user_name = User.objects.get(id=request.session['user_id']).first_name
    charge_total = booking.price_night + booking.price_cleaning + \
        booking.price_servicefee + booking.price_amenitites + booking.price_tax
    context = {
        'user_name': user_name,
        'booking': booking,
        'charge_total': charge_total,
    }
    return render(request, 'booking/view_booking.html', context)


def show_host_place_all_guests(request):
    return render(request, 'booking/success.html')
