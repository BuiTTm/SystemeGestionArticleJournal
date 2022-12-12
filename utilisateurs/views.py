#from xml.etree.ElementTree import tostring
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

from datetime import datetime
from io import BytesIO
import xml.dom.minidom

# def home(request):
#     return render(request, 'journal/home.html')
User = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    #success_url = reverse_lazy("login")
    success_url = reverse_lazy("login")
    template_name = "registration/signupuser.html"


# def signupuser(request):
#     if request.method == 'GET':
#         return render(request, 'utilisateurs/signupuser.html', {'form':UserCreationForm()})
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], nom=request.POST['nom'], prenom=request.POST['prenom'])
#                 #value = user.clean_fields()
#                 #print(f'Value = {value}')
#                 if user.clean_fields():
#                     user.save()
#                     login(request, user)
#                     #Redirect to account page
#                     return redirect('home')
#             except IntegrityError:
#                 return render(request, 'utilisateurs/signupuser.html', {'form':UserCreationForm(), 'error':'Ce courriel est déjà utilisé'})
#             except ValidationError:
#                 return render(request, 'utilisateurs/signupuser.html', {'form':UserCreationForm(), 'error':'Veuillez entrer un courriel valide'})
#         else:
#             return render(request, 'utilisateurs/signupuser.html', {'form':UserCreationForm(), 'error':'Les mots de passe ne correspondent pas ensemble'})

# def loginuser(request):
#     if request.method == 'GET':
#         return render(request, 'utilisateurs/loginuser.html', {'form':AuthenticationForm()})
#     else:
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

#         if user is None:
#             return render(request, 'utilisateurs/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
#         else:
#             login(request, user)
#             #Redirect to account page
#             return redirect('home')

# @login_required
# def logoutuser(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('home')
