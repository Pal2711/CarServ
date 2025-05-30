from django.shortcuts import render,redirect
from .models import *
from .forms import * 
from django.contrib.auth import logout


# Create your views here.

def index(request):
    if request.method == "POST":
        form = bookserviceform(request.POST)
        if form.is_valid():
            form.save()
            print("Your service is book")
            return redirect("/")
        else:
            print(form.errors)
    else:
        form = bookserviceform()
    return render(request, "index.html",{'form': form})


def about(request):
    return render(request, "about.html")

def service(request):
    # for the book servis
    msg = ""
    if request.method == "POST":
        form = bookserviceform(request.POST)
        if form.is_valid():
            form.save()
            print("Your service is book")
            return redirect("service")
        else:
            print(form.errors)
            msg = "Your Service is booked"
    else:
        form = bookserviceform()
    return render(request, "service.html",{"form" : form ,'msg':msg })

def team(request):
    return render(request, "team.html")

def testimonial(request):
    return render(request, "testimonial.html")

def contact(request):
    if request.method == "POST":
        form = usercontactform(request.POST)
        if form.is_valid():
            form.save()
            print("your form is submited")
            return redirect("/")
        else:
            print(form.errors)
    else:
        form = usercontactform()
    return render(request, "contact.html",{'form': form})

def login(request):
    if request.method == "POST":
        unm = request.POST["username"]
        pas = request.POST["password"]

        user = usersignup.objects.filter(username=unm).first() 

        if user:
            print("Login successful")
            request.session["user"] = unm
            request.session["userid"] = user.id
            return redirect("/")
        else:
            print("Error: Login failed!!!")

    return render(request, "login.html")\
    
def userlogout(request):
    logout(request)
    return redirect("/") 

def signup(request):
    if request.method == 'POST':
        form = usersignupform(request.POST) 
        if form.is_valid():
            form.save()
            print("Signup DONE")
            return redirect("/")  
        else:
            print(form.errors)
    else:
        form = usersignupform()  

    return render(request, "signup.html", {'form': form}) 
