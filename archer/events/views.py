from django.shortcuts import render, redirect
from .models import Users
from .forms import StudentForm


# Create your views here.

def home(request):
    name = "Hetav"
    # user = Users.objects.create(first_name="Apple", last_name="Samsung")
    return render(request, 'home.html', {
        "name": name,
    }) 

def dashboard(request):
    return render(request, 'dashboard.html', {})

def login(request):
    return render(request, 'login.html', {})

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the form data to the database
            return redirect('student_form')  # Redirect to the form page after successful submission
    else:
        form = StudentForm()
    return render(request, 'studentform.html', {'form': form})
