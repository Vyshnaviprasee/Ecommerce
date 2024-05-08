# accounts/views.py
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import UserProfile
from store.models import Order, Course
from django.contrib.auth import authenticate, login as auth_login

def register(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
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
            # Create User object
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            
            # Create UserProfile for the newly registered user
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()

            messages.info(request, 'User created successfully')
            return redirect('/')
    else:
        return render(request, 'register.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  # Redirect to the homepage or any other appropriate page
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def user_logout(request):
    auth_logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('index')  # Redirect to the homepage or any other appropriate page
  # Redirect to the homepage or any other appropriate page


def view_profile(request):
    try:
        # Retrieve the user's profile based on the currently logged-in user
        user_profile = UserProfile.objects.get(user=request.user)
        
        # Query the Order model to get the courses purchased by the user
        user_orders = Order.objects.filter(user=request.user)
        purchased_courses = []
        for order in user_orders:
            # Append a dictionary with course attributes to purchased_courses list
            purchased_courses.append({
                'title': order.course.course_name,
                'description': order.course.desc,
                'price': order.course.price,
                'payment_status': order.get_status_display()  # Use get_status_display() to get the display value of status field
            })

        return render(request, 'view_profile.html', {'user_profile': user_profile, 'purchased_courses': purchased_courses})
    except UserProfile.DoesNotExist:
        return HttpResponse("UserProfile does not exist for this user.")
