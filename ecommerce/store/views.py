from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Category, Order
from accounts.models import User
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
    course = get_object_or_404(Course, slug=course_slug)
    if 'cart' not in request.session:
        request.session['cart'] = []
    request.session['cart'].append(course.id)
    request.session.modified = True
    return redirect('cart')

def cart(request):
    cart_course_ids = request.session.get('cart', [])
    courses_in_cart = Course.objects.filter(id__in=cart_course_ids)
    total_price = sum(course.price for course in courses_in_cart)
    context = {
        'courses_in_cart': courses_in_cart,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

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
        # Calculate total price
        total_price = sum(course.price for course in courses_in_cart)
        # Create an order for each course in the cart
        for course in courses_in_cart:
            order = Order.objects.create(
                user=request.user,
                course=course,
                quantity=1,  # You may adjust this based on your requirements
                total_price=course.price  # Assuming each course's total price is its price
            )
        # Clear the cart after placing the order
        del request.session['cart']
        # Redirect the user to the homepage
        return redirect('payment_confirmation')
    return render(request, 'checkout.html')


def payment_confirmation(request):
    # Render payment confirmation page
    return render(request, 'payment_confirmation.html')
