from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout  # Rename to avoid conflict
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return render(request, 'register.html')
        elif password != confirm_password:
            messages.info(request, 'Passwords do not match')
            return render(request, 'register.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.info(request, 'User created successfully')
            return redirect('/')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Renamed login function
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):  # Renamed to avoid conflict
    auth_logout(request)  # Use Django's built-in logout function
    messages.info(request, 'Logged out successfully')
    return redirect('/') # Redirecting to login page after logout