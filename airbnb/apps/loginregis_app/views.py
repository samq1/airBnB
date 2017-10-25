from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from models import User, UserManager, Language
from django.contrib import messages
from datetime import date
from django.urls import reverse
import json


def main_login(request):
# MAIN LOGIN PAGE ---------------------------------------
    print ('YOURE AT THE LOGIN PAGE!')

    return render(request, 'loginregis_app/main_login.html')



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
        return redirect(reverse('login:login_index'))
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    
    return redirect(reverse('login:success'))

def user_profile(request):
# USER PROFILE --------------------------------------------
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }

    return render(request, 'loginregis_app/user_profile.html', context)

def edit(request, User_id):
# EDIT USER PROFILE -----------------------------------------
    print "YOURE AT THE EDIT PAGE"
    context = {
    'user': User.objects.get(id=User_id)
    }
    return render(request, 'loginregis_app/edit_profile.html', context)

def process(request):
# USER LOGGING IN (PROCESSING INTO DATABASE) ---------------
    result = User.objects.login_validator(request.POST)
    print result
    if type(result) == list:
        if len(result) > 0:
            messages.error(request, result)
            return redirect(reverse('login:main_login'))

    request.session['user_id'] = result.id
    messages.success(request, "You successfully logged in!") 
    return redirect(reverse('login:user_profile'))

def update(request, User_id):
    print User_id
    person = User.objects.get(id=User_id)
    person.first_name = request.POST.get('first_name', "")
    person.last_name = request.POST.get('last_name', "")
    # person.email = request.POST.get('email', "")
    person.save()
    
    return redirect(reverse('login:user_profile'))

def clear(request):
# USER LOGGING OUT ------------------------------------------
    del request.session['user_id']

    return redirect('/')