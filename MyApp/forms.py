from django.db.models import fields
from .models import *
from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Login_Form(ModelForm):
    email_id=CharField()
    password=CharField()
    class Meta:
        model=Login
        fields=("email_id","password")
        attrs={}
class Sign_Up_Form(UserCreationForm):
    #  username=CharField()
    #  email_id=CharField()
    #  password=CharField(max_length=10)
     class Meta:
         model=User
         fields=("username","email","password1","password2")
