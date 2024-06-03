# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('add-to-cart/<str:category_slug>/<str:course_slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('delete-from-cart/<int:course_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('checkout/', views.checkout, name='checkout'),  # Define the checkout URL pattern
    path('payment-confirmation/<int:total_price>/', views.payment_confirmation, name='payment_confirmation'),
    path('course/<int:course_id>/tutorials/', views.course_tutorials, name='course_tutorials'),
    path('tutorial/<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
    path('category/<slug:category_slug>/<slug:course_slug>/', views.course_detail, name='course_detail'),




]
