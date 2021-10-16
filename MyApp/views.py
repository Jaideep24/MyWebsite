from django.http import response
from django.shortcuts import redirect, render
import requests
from .models import *
from .forms import *
from django.contrib.auth import login as auth_login,authenticate
# Create your views here.
timepass=False

def main(request):
    API_key="88d8899a3f654a0d4e9dd0db40d5728e"
    global timepass
    form=None
    email=None
    if request.method=="POST":
        if "city" in request.POST and "email_id" not in request.POST and "username" not in request.POST:
            city_name=request.POST["city"]
            city_data=get_city(city_name)
            timepass=True
        if "city"  not in request.POST and "email_id" in request.POST:
            form=Login_Form(request.POST)
            if form.is_valid():
                form.save()
                #username=form.cleaned_data.get("username")
                email_to_find=form.cleaned_data.get("email_id")
                password=form.cleaned_data.get("password")
                usernames=User.objects.filter(email=email_to_find)
                email=email_to_find
                for i in usernames[:]:
                    username=i
                    user=authenticate(username=username, password=password)
                    if user==None:
                        email="Anonymous"
                    else:
                        auth_login(request,user)
                        print("logged in as",user.email)
                        break
            else:
                form=Login_Form()
        elif "city" not in request.POST and "username" in request.POST:
            print(request.POST)
            form=Sign_Up_Form(request.POST)
            print(form.fields)
            if form.is_valid():
                print("the form is valid")
                if not User.objects.filter(username=form.cleaned_data["username"]).exists():
                    print("if i dont work you are dead")
                    form.save()
                    username=form.cleaned_data.get("username")
                    email=form.cleaned_data.get("email")
                    password=form.cleaned_data.get("password1")
                    
    if timepass==True:
        city_data=Weather_city.objects.all().last()
    else:
        city_data="Mumbai"

    response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_data}&appid={API_key}&units=metric")
    data=response.json()
    weather_data={"main":data["main"], "icon":data["weather"][0]["icon"],"name":data["name"],"form":form,"email":email}
    return(weather_data)

def get_city(city_name):
    city_data=Weather_city.objects.create(city=city_name)
    city_data.save()
    return(Weather_city.objects.all().last())
def homepage(request):
    weather_data=main(request)
    return(render(request, "MyApp/index.html", weather_data))
def firstRide(request):
   weather_data=main(request)
   return(render(request, "MyApp/Imagica.html", weather_data))
def secondRide(request):
    weather_data=main(request)
    return(render(request, "MyApp/Kidzania.html", weather_data))
def thirdRide(request):
    weather_data=main(request)
    return(render(request, "MyApp/Essel World.html", weather_data))
def fourthRide(request):
    weather_data=main(request)
    return(render(request, "MyApp/Water Kingdom.html", weather_data))   
def fifthRide(request):
    weather_data=main(request)
    return(render(request, "MyApp/Snow World.html", weather_data))
def login(request):
    weather_data=main(request)
    if weather_data["email"]==None:
        weather_data["form"]=Login_Form()
        return(render(request, "MyApp/Login.html", weather_data))
    elif weather_data["email"]=="Anonymous":
        weather_data["form"]=Sign_Up_Form()
        return(redirect("signup"))
    else:
        print(weather_data["email"])
        return(redirect("/"))
def sign_up(request):
    weather_data=main(request)
    print(weather_data["email"])
    if weather_data["email"]==None:
        weather_data["form"]=Sign_Up_Form()
        return(render(request, "MyApp/Sign up.html", weather_data))
    else:
        weather_data["form"]=Login_Form()
        print("I am iron man")
        return(redirect("login"))
