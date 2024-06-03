from django.shortcuts import render
from django.http import HttpResponse
from store.models import Course, Category, Order


# Create your views here.

def index(request):
    # Get all available courses ordered by priority and limit to 4
    featured_courses = Course.objects.filter(is_available=True).order_by('-priority')[:3]
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Query the Order model to get the courses purchased by the user
        user_orders = Order.objects.filter(user=request.user)
        purchased_courses = [order.course for order in user_orders]
    else:
        purchased_courses = []  # If the user is not authenticated, initialize an empty list
        
    categories = Category.objects.all()
    
    context = {
        'featured_courses': featured_courses,  # Pass featured courses to the template
        'categories': categories,
        'purchased_courses': purchased_courses  # Pass purchased courses to the template
    }
    return render(request, 'index.html', context)


def course(request):
    try:
        courses = Course.objects.filter(is_available=True)
    except Course.DoesNotExist:
        courses = None
    context = {
        'courses': courses
    }
    return render(request, 'course.html', context) 

