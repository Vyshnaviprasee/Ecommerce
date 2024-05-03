from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    desc = models.TextField(max_length=500, blank=True)
    img = models.ImageField(upload_to='category/', default='default_category_image.jpg')  # Example default value

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
