from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from ..loginregis_app.models import *
from django.contrib import messages
from datetime import date
from django.conf import settings
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
import json


def review_users(request, User_id):
# MAIN REVIEW PAGE ---------------------------------------
    print ('YOURE AT THE REVIEW PAGE!')

    context = {
    'User': User.objects.get(id=User_id)
    }

    return render(request, 'review/review_users.html', context)

def review_places(request, Place_id):
# MAIN REVIEW PLACE PAGE ---------------------------------------
    print ('YOURE AT THE REVIEW PAGE!')
    print Place_id
    Place_id = Place_id
    context = {
    'Cleanliness': Cleanliness.choices,
    'Rating': Rating.choices,
    'Place_id': Place_id,
    }

    return render(request, 'review/review_places.html', context)

def process_host_user_review(request, User_id):
# REVIEW USER/HOST -----------------------------------------
    print "GOT TO USER REVIEW"
    print User_id
    if 'user_id' not in request.session:
        return redirect(reverse('login:main_login'))

    if request.method == 'POST':
        host = User.objects.get(id=request.session['user_id'])
        customer = User.objects.get(id=User_id)
        comment_user = request.POST['comment_user']
        
        Review_User.objects.create(comment_user=comment_user, reviewer=host, user_being_reviewed=customer)

        messages.success(request, "You successfully reviewed!") 
        return redirect(reverse('login:user_profile'))

    return redirect(reverse('login:main_login'))

def process_placereview(request, Place_id):
# REVIEW PLACE ---------------------------------------------
    print "GOT TO PLACE REVIEW"
    print Place_id

    if 'user_id' not in request.session:
        return redirect(reverse('login:main_login'))

    if request.method == 'POST':
        is_location_accuracy = False
        is_recommend = False

        if 'is_location_accuracy' in request.POST:
            is_location_accuracy = True
        if 'is_recommend' in request.POST:
            is_recommend = True
        
        customer = User.objects.get(id=request.session['user_id'])
        place_staying = Place.objects.get(id=Place_id)
        comment_place = request.POST['comment_place']
        
        Review_Place.objects.create(comment_place=comment_place, is_location_accuracy=is_location_accuracy, is_recommend=is_recommend, reviewer=customer, place=place_staying)

        messages.success(request, "You successfully reviewed!") 
        return redirect(reverse('login:user_profile'))

    return redirect(reverse('login:user_profile'))