from xml.etree.ElementTree import tostring
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
#from .forms import SoumissionArticleForm
#from .models import SoumissionArticle
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from io import BytesIO

import xml.dom.minidom

# def home(request):
#     return render(request, 'journal/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'utilisateurs/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                #Redirect to account page
                return redirect('home')
            except IntegrityError:
                return render(request, 'utilisateurs/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'utilisateurs/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'utilisateurs/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'utilisateurs/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            #Redirect to account page
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
