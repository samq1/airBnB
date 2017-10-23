from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from ..loginregis_app.models import User, UserManager
from django.contrib import messages
from datetime import date
from django.urls import reverse


def index(request):

    return render(request, 'airbnb/index.html')

