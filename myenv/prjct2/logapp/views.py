from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth



# Create your views here.

def home(request):  
    return render(request,'index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password=request.POST['confirm_password']

        # Check if 'confirm_password' key exists in the POST data
        # if 'confirm_password' in request.POST:
        #     confirm_password = request.POST['confirm_password']
        # else:
        #     messages.info(request, 'Please confirm your password')
        #     return redirect('signup')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('signup')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Account created successfully')
                return redirect('login_user')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('signup')

    # If it's a GET request, render the signup page
    return render(request, 'signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('logout_user')
    else:
        return render(request,'login.html')
    



def logout_user(request):
    auth.logout(request)
    return redirect('home')