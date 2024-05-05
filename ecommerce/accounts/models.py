from django.db import models
from django.contrib.auth.models import User
from store.models import Course  # Import the Course model from the store app

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    selected_courses = models.ManyToManyField(Course)

    # Add any other fields you need for the user profile
