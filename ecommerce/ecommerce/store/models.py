from django.db import models
from category.models import Category

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    course_img = models.ImageField(upload_to='course/')
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    desc = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.course_name