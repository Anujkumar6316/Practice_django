from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
# Create your models here.

class Registration(UserCreationForm):
    email = forms.EmailField(label='Email')
    