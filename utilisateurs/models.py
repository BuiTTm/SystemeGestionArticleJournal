#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
#from django import forms
from django.utils.translation import gettext_lazy as _
#from django.contrib.auth.models import User


class CustomUser(AbstractUser):
#class CustomUser(AbstractBaseUser):
    username = models.EmailField(unique=True, null=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nom', 'prenom']
    #age = models.PositiveIntegerField(null=True, blank=True)
    est_evaluateur = models.BooleanField(null=True, default=False)
