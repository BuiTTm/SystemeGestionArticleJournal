from xml.etree.ElementTree import tostring
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import SoumissionArticleForm
from .models import SoumissionArticle
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from io import BytesIO

import xml.dom.minidom

def home(request):
    return render(request, 'journal/home.html')

