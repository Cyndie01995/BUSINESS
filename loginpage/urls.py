from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Signup', views.signup, name='Signup'),
    path('Signin', views.signin, name='signin'),
    path('Signout', views.signout, name='Signout'),    
]
