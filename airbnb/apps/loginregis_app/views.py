from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from models import User, UserManager
from django.contrib import messages
from datetime import date
import json

def index(request):

    return render(request, 'loginregis_app/index.html')

def register(request):
    result = User.objects.register_valid(request.POST)
    print result
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    
    return redirect("/success")

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