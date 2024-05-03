# views.py
from django.shortcuts import get_object_or_404, render
from .models import Course, Category

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
        'course': course
    }
    return render(request, 'course_detail.html', context)
