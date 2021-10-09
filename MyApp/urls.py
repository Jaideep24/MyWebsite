
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("",homepage, name="home"),
    path("1/",firstRide),
    path("2/",secondRide),
    path("3/",thirdRide),
    path("4/",fourthRide),
    path("5/",fifthRide),
    path("login",login, name="login"),
    path("signup",sign_up, name="signup")
]
