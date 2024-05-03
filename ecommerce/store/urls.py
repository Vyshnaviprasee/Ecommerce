# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('add-to-cart/<str:category_slug>/<str:course_slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),  # Define the checkout URL pattern
    path('payment-confirmation/', views.payment_confirmation, name='payment_confirmation'),  # Define the payment confirmation URL pattern

]
