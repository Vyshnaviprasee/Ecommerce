from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from accounts.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def store(request, category_slug=None):
    courses = Course.objects.filter(is_available=True)
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        courses = courses.filter(category=category)
    
    course_count = courses.count()
    
    context = {
        'courses': courses,
        'categories': categories,
        'course_count': course_count
    }
    return render(request, 'store.html', context)

def course_detail(request, category_slug, course_slug):
    category = get_object_or_404(Category, slug=category_slug)
    course = get_object_or_404(Course, category=category, slug=course_slug)
    
    context = {
        'category': category,
        'course': course
    }
    return render(request, 'course_detail.html', context)

def add_to_cart(request, category_slug, course_slug):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, slug=course_slug)
        
        if 'cart' not in request.session:
            request.session['cart'] = []
    
        cart_course_ids = request.session.get('cart', [])
        if course.id not in cart_course_ids:
            request.session['cart'].append(course.id)
            request.session.modified = True
    
        return redirect('cart')
    else:
        messages.info(request, 'Please login to add course to cart')
        return redirect('login')


def cart(request):
    cart_course_ids = request.session.get('cart', [])
    courses_in_cart = Course.objects.filter(id__in=cart_course_ids)
    total_price = sum(course.price for course in courses_in_cart)
    context = {
        'courses_in_cart': courses_in_cart,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

def delete_from_cart(request, course_id):
    if 'cart' in request.session:
        cart_course_ids = request.session.get('cart')
        if course_id in cart_course_ids:
            cart_course_ids.remove(course_id)
            request.session['cart'] = cart_course_ids
            request.session.modified = True
    return redirect('cart')

def checkout(request):
    if request.POST:
        # Retrieve the course IDs from the session
        cart_course_ids = request.session.get('cart', [])
        # Check if the cart is empty
        if not cart_course_ids:
            # Redirect the user back to the cart page or any other appropriate page
            return redirect('cart')
        # Retrieve the courses in the cart
        courses_in_cart = Course.objects.filter(id__in=cart_course_ids)
        # Calculate total price and create orders
        total_price = 0  # Initialize total price
        for course_id in cart_course_ids:
            course = Course.objects.get(id=course_id)
            total_price += course.price  # Add course price to total price
            Order.objects.create(
                user=request.user,
                course=course,
                quantity=1,  # You may adjust this based on your requirements
                total_price=course.price  # Assuming each course's total price is its price
            )
        # Clear the cart after placing the order
        del request.session['cart']
        # Redirect the user to the payment confirmation page with the total_price parameter
        return redirect('payment_confirmation', total_price=total_price)
    return render(request, 'checkout.html')



def payment_confirmation(request, total_price):
    # Render payment confirmation page with the total_price context variable
    return render(request, 'payment_confirmation.html', {'total_price': total_price})

# store/views.py

# views.py

def course_tutorials(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        tutorials = Tutorial.objects.filter(course=course)
        
        # Retrieve the count of tutorials related to the course
        total_modules = tutorials.count()
        
        context = {
            'course': course,
            'tutorials': tutorials,
            'total_modules': total_modules  # Add total modules count to the context
        }
        return render(request, 'course_tutorials.html', context)
    except Course.DoesNotExist:
        return HttpResponse("Course does not exist.")

# views.py

def tutorial_detail(request, tutorial_id):
    # Get the tutorial object
    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    
    # Get the course of the tutorial
    course = tutorial.course
    
    # Get up next tutorials within the same course, excluding the current tutorial
    up_next_tutorials = Tutorial.objects.filter(course=course).exclude(pk=tutorial.pk)[:5]
    
    context = {
        'tutorial': tutorial,
        'up_next_tutorials': up_next_tutorials
    }
    return render(request, 'tutorial_details.html', context)
