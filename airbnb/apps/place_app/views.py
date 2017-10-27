# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from ..loginregis_app.models import *
from django.contrib import messages
import ast
import decimal
from django.core.files.storage import FileSystemStorage


def show_place(request, place_id):
    # if "user_id" in request.session:
    #     return redirect('/users/all')
    # else:
    #     return redirect('/users')
    try:
        place = Place.objects.get(id=place_id)
        picture = place.place_pictures.first()
    except:
        return redirect(reverse('places:does_not_exist'))
    context = {
        "users": User.objects.all(),
        "place1": place,
        "picture": picture.image.url,
        "today": datetime.today().strftime("%Y-%m-%d"),
    }
    print place
    print picture

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

def become_host(request):
    if 'user_id' not in request.session:
        return redirect(reverse('login:main_login'))
    user = User.objects.get(id=request.session['user_id'])

    context = {
        'user': User.objects.get(id=request.session['user_id']),

    }
    
    return render(request, "place/create_place.html", context)

def adding_host(request):
    if 'user_id' not in request.session:
        return redirect(reverse('login:main_login'))

    if request.method == 'POST':

        is_smoking_allowed = False
        is_amenities_free_parking = False
        is_family_amenities_baby_monitor = False
        is_familty_amenities_bathtub = False
        is_familty_amenities_changing_table = False
        is_familty_amenities_crib = False
        is_familty_amenities_fireguards = False
        is_familty_amenities_high_chair = False
        is_familty_amenities_game_console = False
        is_familty_amenities_stair_gates = False
        is_amenities_pool = False
        is_amenities_pets_allowed = False
        is_amenities_breakfast = False
        is_amenities_gym = False
        is_amenities_hot_tub = False
        is_amenities_washer = False
        is_amenities_dryer = False
        is_amenities_internet = False
        is_amenities_wheelchair = False
        is_amenities_elevator = False
        is_amenities_fireplace = False
        is_amenities_air_conditioning = False
        is_amenities_cable_tv = False
        is_amenities_iron = False
        is_amenities_linen_essentials = False
        is_amenities_kitchen = False
        is_amenities_tv = False
        is_amenities_hair_dryer = False
        is_amenities_heating = False
        

        user = User.objects.get(id=request.session['user_id'])
        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        description = request.POST['description']
        neighborhood = request.POST['neighborhood']
        check_in_time = request.POST['check_in_time']
        check_out_time = request.POST['check_out_time']
        house_rules = request.POST['house_rules']

        if 'is_smoking_allowed' in request.POST:
            is_smoking_allowed = True
        if 'is_amenities_free_parking' in request.POST:
            is_amenities_free_parking = True
        if 'is_family_amenities_baby_monitor' in request.POST:
            is_family_amenities_baby_monitor = True
        if 'is_familty_amenities_bathtub' in request.POST:
            is_familty_amenities_bathtub = True
        if 'is_familty_amenities_changing_table' in request.POST:
            is_familty_amenities_changing_table = True
        if 'is_familty_amenities_crib' in request.POST:
            is_familty_amenities_crib = True
        if 'is_familty_amenities_fireguards' in request.POST:
            is_familty_amenities_fireguards = True
        if 'is_familty_amenities_high_chair' in request.POST:
            is_familty_amenities_high_chair = True
        if 'is_familty_amenities_game_console' in request.POST:
            is_familty_amenities_game_console = True
        if 'is_familty_amenities_stair_gates' in request.POST:
            is_familty_amenities_stair_gates = True
        if 'is_amenities_pool' in request.POST:
            is_amenities_pool = True
        if 'is_amenities_pets_allowed' in request.POST:
            is_amenities_pets_allowed = True
        if 'is_amenities_breakfast' in request.POST:
            is_amenities_breakfast = True
        if 'is_amenities_gym' in request.POST:
            is_amenities_gym = True
        if 'is_amenities_hot_tub' in request.POST:
            is_amenities_hot_tub = True
        if 'is_amenities_washer' in request.POST:
            is_amenities_washer = True
        if 'is_amenities_dryer' in request.POST:
            is_amenities_dryer = True
        if 'is_amenities_internet' in request.POST:
            is_amenities_internet = True
        if 'is_amenities_wheelchair' in request.POST:
            is_amenities_wheelchair = True
        if 'is_amenities_elevator' in request.POST:
            is_amenities_elevator = True
        if 'is_amenities_fireplace' in request.POST:
            is_amenities_fireplace = True
        if 'is_amenities_air_conditioning' in request.POST:
            is_amenities_air_conditioning = True
        if 'is_amenities_cable_tv' in request.POST:
            is_amenities_cable_tv = True
        if 'is_amenities_iron' in request.POST:
            is_amenities_iron = True
        if 'is_amenities_linen_essentials' in request.POST:
            is_amenities_linen_essentials = True
        if 'is_amenities_kitchen' in request.POST:
            is_amenities_kitchen = True
        if 'is_amenities_tv' in request.POST:
            is_amenities_tv = True
        if 'is_amenities_hair_dryer' in request.POST:
            is_amenities_hair_dryer = True
        if 'is_amenities_heating' in request.POST:
            is_amenities_heating = True
        

        cancellation_policy = request.POST['cancellation_policy']
        price_night = decimal.Decimal(request.POST['price_night'])
        price_cleaning = decimal.Decimal(request.POST['price_cleaning'])
        price_servicefee = 99.00
        price_tax = 1
        price_amenitites = decimal.Decimal(request.POST['price_amenitites'])

        NewPlace = Place.objects.create(
            name=name,
            address=address, 
            city=city, 
            state=state, 
            zipcode=zipcode, 
            country=country, 
            description=description, 
            neighborhood=neighborhood, 
            check_in_time=check_in_time, 
            check_out_time=check_out_time, 
            is_smoking_allowed=is_smoking_allowed, 
            house_rules=house_rules, 
            is_amenities_free_parking=is_amenities_free_parking, 
            is_family_amenities_baby_monitor=is_family_amenities_baby_monitor, 
            is_familty_amenities_bathtub=is_familty_amenities_bathtub, 
            is_familty_amenities_changing_table=is_familty_amenities_changing_table, 
            is_familty_amenities_crib=is_familty_amenities_crib, 
            is_familty_amenities_fireguards=is_familty_amenities_fireguards, 
            is_familty_amenities_high_chair=is_familty_amenities_high_chair, 
            is_familty_amenities_game_console=is_familty_amenities_game_console, 
            is_familty_amenities_stair_gates=is_familty_amenities_stair_gates,
            is_amenities_pool=is_amenities_pool,
            is_amenities_pets_allowed=is_amenities_pets_allowed,
            is_amenities_breakfast=is_amenities_breakfast,
            is_amenities_gym=is_amenities_gym, 
            is_amenities_hot_tub=is_amenities_hot_tub, 
            is_amenities_washer=is_amenities_washer, 
            is_amenities_dryer=is_amenities_dryer, 
            is_amenities_internet=is_amenities_internet, 
            is_amenities_wheelchair=is_amenities_wheelchair, 
            is_amenities_elevator=is_amenities_elevator, 
            is_amenities_fireplace=is_amenities_fireplace, 
            is_amenities_air_conditioning=is_amenities_air_conditioning, 
            is_amenities_cable_tv=is_amenities_cable_tv, 
            is_amenities_iron=is_amenities_iron, 
            is_amenities_linen_essentials=is_amenities_linen_essentials, 
            is_amenities_kitchen=is_amenities_kitchen, 
            is_amenities_tv=is_amenities_tv, 
            is_amenities_hair_dryer=is_amenities_hair_dryer, 
            is_amenities_heating=is_amenities_heating, 
            cancellation_policy=cancellation_policy, 
            price_night=price_night, 
            price_cleaning=price_cleaning, 
            price_amenitites=price_amenitites, 
            price_servicefee=price_servicefee,
            price_tax=price_tax, 
            host=user
        )

        place_id = NewPlace.id
        messages.success(request, "You successfully created your crib!") 
        return redirect(reverse('places:upload_page', kwargs={'place_id':place_id}))

    return render(request, "place/create_place.html", context)


def upload_page(request, place_id):
# UPLOAD PAGE ------------------------------------------
    user = User.objects.get(id=request.session['user_id']),

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'place': Place.objects.get(id=place_id),
        
    }

    
    return render(request, 'place/upload_pic.html', context)

def upload(request, place_id):
# UPDATING PLACE PROFILE ------------------------------------------
    # print User_id
    if request.method == 'POST':
        person = User.objects.get(id=request.session['user_id'])
        place = Place.objects.get(id=place_id)
        caption = request.POST['caption']
        myfile = request.FILES['myfile']
        person.image = myfile
        Picture.objects.create(caption=caption, place=place, user=person, image=myfile)
        place.save()
        

        messages.success(request, "You successfully uploaded!") 
        return redirect(reverse('places:show', kwargs={'place_id':place_id}))

    return render(request, 'place/upload_pic.html')


def simple_upload(request):
# UPLOAD PHOTOS ------------------------------------------
    if request.method == 'POST' and request.FILES['myfile']:
        print 'YOURE UPLOADING!'
        myfile = request.FILES['myfile']
        print myfile
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print filename
        uploaded_file_url = fs.url(filename)
        print uploaded_file_url
        return redirect(reverse('places:show', kwargs={'place_id':place_id}))

        # place = Place.objects.get(id=Place_id)
        # person = User.objects.get(id=User_id)
        # myfile = request.FILES['myfile']
        # person.image = myfile
    return render(request, 'loginregis_app/edit_profile.html')