from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from category.models import Category

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    course_img = models.ImageField(upload_to='course/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    study_material = models.FileField(upload_to='study_materials/', default=timezone.now, blank=True, null=True)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.course_name

class Order(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Unpaid')

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username}"

# store/models.py

class Tutorial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='tutorial_thumbnails', null=True, blank=True)
    module_number = models.PositiveIntegerField(default=1)  # Default value changed to 1

    def __str__(self):
        return self.title

