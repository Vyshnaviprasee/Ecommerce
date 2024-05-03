from django.shortcuts import render
from django.http import HttpResponse
from store.models import Course, Category

# Create your views here.

def index(request):
    courses = Course.objects.filter(is_available=True)
    categories = Category.objects.all()
    context = {
        'courses': courses,
        'categories': categories
    }
    return render(request, 'index.html', context)

def course(request):
    courses = Course.objects.filter(is_available=True)
    context = {
        'courses': courses  # Changed 'course' to 'courses'
    }
    return render(request, 'course.html', context) 