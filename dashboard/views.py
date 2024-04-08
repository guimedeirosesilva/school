from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from .utils import *
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


# index view
def index(request):
    return render(request, "dashboard/index.html")


# login view
def login_view(request):
    # GET
    if request.method == "GET":
        form = LoginForm()

        return render(request, "dashboard/login.html", {
            "form": form
        })
    
    # POST
    elif request.method == "POST":
        # login the user
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                form = LoginForm()
                return render(request, "dashboard/login.html", {
                    "form": form,
                    "message": "Invalid username and/or password."
                })
            


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    # GET
    if request.method == "GET":
        form = RegisterForm()

        return render(request, "dashboard/register.html", {
            "form": form
        })

    # POST
    elif request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            confirmation = form.cleaned_data["confirmation"]

            # Confirm password
            if password != confirmation:
                return render(request, "dashboard/register.html", {
                    "message": "Passwords don't match."
                })
            
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                return render(request, "dashboard/register.html", {
                    "message": "Username already taken."
                })
            
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
