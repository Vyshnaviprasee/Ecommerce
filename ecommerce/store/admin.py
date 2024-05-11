# store/admin.py

from django.contrib import admin
from .models import Course, Order, Tutorial

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'module_number')  # Customize the fields displayed in the admin list view


class TutorialInline(admin.TabularInline):
    model = Tutorial
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('course_name',)}
    list_display = ('course_name', 'category', 'price', 'stock', 'created_date', 'modified_date',  'slug')
    inlines = [TutorialInline]  # Add TutorialInline to CourseAdmin

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_price')  # Replace 'total_amount' with 'total_price'
    list_filter = ('user', 'order_date')
    search_fields = ('user__username', 'id')


admin.site.register(Course, CourseAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tutorial, TutorialAdmin)