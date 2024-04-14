from django.shortcuts import render, redirect
from .models import People
from django.contrib.auth import logout
# Create your views here.

def home(request):
    name = "Hetav"
    user = People.objects.create(first_name="Apple", last_name="Samsung")
    return render(request, 'home.html', {
        "name": name,
    }) 

def dashboard(request):
    return render(request, 'dashboard.html', {})

def login(request):
    return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect("/")
