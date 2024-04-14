from django.shortcuts import render

# Create your views here.

def home(request):
    name = "Hetav"
    return render(request, 'home.html', {
        "name": name,
    }) 

def dashboard(request):
    return render(request, 'dashboard.html', {})