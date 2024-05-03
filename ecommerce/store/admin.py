from django.contrib import admin
from . models import Course, Order

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('course_name',)}
    list_display = ('course_name', 'category', 'price', 'stock', 'created_date', 'modified_date',  'slug')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_amount')
    list_filter = ('user', 'order_date')
    search_fields = ('user__username', 'id')


admin.site.register(Course)
admin.site.register(Order)
