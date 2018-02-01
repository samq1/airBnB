from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.db.models import Count
from django.contrib import messages
from datetime import date
from django.conf import settings
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
import json


def main_login(request):
# MAIN LOGIN PAGE ---------------------------------------
    print ('YOURE AT THE LOGIN PAGE!')

    return render(request, 'loginregis_app/main_login.html')


def main_logout(request):
    del request.session['user_id']
    del request.session['username']
    del request.session['user_first_name']
    del request.session['user_last_name']
    if 'user_is_host' in request.session:
        del request.session['user_is_host']
    return redirect(reverse('login:main_login'))



def register_page(request):
# MAIN REGISTER PAGE ---------------------------------------
    print ('YOURE AT THE REGISTER PAGE!')
    
    context = {
        'Languages': Language.choices
    }

    return render(request, 'loginregis_app/register.html', context)

def register(request):
# NEW USER REGISTER ---------------------------------------
    result = User.objects.register_valid(request.POST)
    # print result
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect(reverse('login:register_page'))

    request.session['user_id'] = result.id
    request.session['username'] = result.username
    request.session['user_first_name'] = result.first_name
    request.session['user_last_name'] = result.last_name
    messages.success(request, "Successfully registered!")
    
    return redirect(reverse('login:user_profile'))

def user_profile(request):
# USER PROFILE --------------------------------------------
    user = User.objects.get(id=request.session['user_id'])
    print user.state
    other_users = User.objects.exclude(id=request.session['user_id'])
    users_around_you = User.objects.filter(state=user.state).exclude(id=request.session['user_id'])
    my_travels = Booking.objects.filter(guest=user).values('place__id', 'place__name', 'place__city').distinct()
    place = Place.objects.all()
    print my_travels

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'other_users': other_users,
        'users_around_you': users_around_you,
        'my_travels': my_travels,
        'place': place

    }

    return render(request, 'loginregis_app/user_profile.html', context)

def edit(request, User_id):
# EDIT USER PROFILE -------------------------------------------
    print "YOURE AT THE EDIT PAGE"
    
    context = {
    'user': User.objects.get(id=User_id)
    }
    return render(request, 'loginregis_app/edit_profile.html', context)

def process(request):
# USER LOGGING IN (PROCESSING INTO DATABASE) -------------------
    result = User.objects.login_validator(request.POST)
    print result
    if type(result) == list:
        if len(result) > 0:
            messages.error(request, result)
            return redirect(reverse('login:main_login'))
    
    # check if the logged in user is also a host
    hosted_places = Place.objects.filter(host = result)
    num_hosted_places = hosted_places.count()

    request.session['user_id'] = result.id
    request.session['username'] = result.username
    request.session['user_first_name'] = result.first_name
    request.session['user_last_name'] = result.last_name
    if num_hosted_places > 0:
        request.session['user_is_host'] = num_hosted_places
    messages.success(request, "You successfully logged in!") 
    return redirect(reverse('login:user_profile'))

def update(request, User_id):
# UPDATING USER PROFILE ------------------------------------------
    print User_id
    person = User.objects.get(id=User_id)
    myfile = request.FILES['myfile']
    person.image = myfile
    person.first_name = request.POST.get('first_name', "")
    person.last_name = request.POST.get('last_name', "")
    # person.email = request.POST.get('email', "")
    person.save()
    
    return redirect(reverse('login:user_profile'))

def show(request, User_id):
#To display OTHER User -----------------------------------------
    that_user = User.objects.get(id=User_id)
    other_users = User.objects.exclude(id=User_id)
    users_around_them = User.objects.filter(state=that_user.state).exclude(id=User_id)
    my_travels = Booking.objects.filter(guest=that_user).values('place__id', 'place__name', 'place__city').distinct()

    context = {
        'User': User.objects.get(id=User_id),
        'other_users': other_users,
        'users_around_them': users_around_them,
        'my_travels': my_travels
    }

    return render(request,'loginregis_app/show_profile.html', context)

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
        return redirect(reverse('login:user_profile'))

    return render(request, 'loginregis_app/edit_profile.html')


def clear(request):
# USER LOGGING OUT ------------------------------------------
    del request.session['user_id']

    return redirect('/')
