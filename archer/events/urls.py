from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('login', views.login, name="login"),
    path('student-form/', views.student_form, name='student_form'),

]
