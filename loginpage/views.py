from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render (request, 'loginpage/home.html')
def signup(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        # username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request, "User created successfully")
        
        return redirect('signin')
    return render(request, 'loginpage/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'loginpage/home.html', {'fname': fname})
        else:
            messages.error(request, "Username or Password is incorrect")
    return render(request, 'loginpage/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')
