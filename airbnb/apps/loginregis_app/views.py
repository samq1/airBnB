from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from models import User, UserManager, Language
from django.contrib import messages
from datetime import date
from django.urls import reverse
import json

def index(request):
    print ('YOURE AT THE REGISTER PAGE!')
    
    context = {
        'Languages': Language.choices
    }

    return render(request, 'loginregis_app/index.html', context)

def main_login(request):
    print ('YOURE AT THE LOGIN PAGE!')

    return render(request, 'loginregis_app/main_login.html')

def register(request):
    result = User.objects.register_valid(request.POST)
    print result
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect(reverse('login:login_index'))
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    
    return redirect(reverse('login:success'))

def success(request):

    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }

    return render(request, 'loginregis_app/success.html', context)


def process(request):
    result = User.objects.login_validator(request.POST)
    print result
    if type(result) == list:
        if len(result) > 0:
            messages.error(request, result)
            return redirect('/')

    request.session['user_id'] = result.id
    messages.success(request, "You successfully logged in!") 
    return redirect("/success")

def clear(request):
    del request.session['user_id']

    return redirect('/')