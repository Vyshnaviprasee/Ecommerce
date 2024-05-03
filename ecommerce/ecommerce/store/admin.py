from django.contrib import admin
from . models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('course_name',)}
    list_display = ('course_name', 'category', 'price', 'stock', 'created_date', 'modified_date',  'slug')
admin.site.register(Course)

