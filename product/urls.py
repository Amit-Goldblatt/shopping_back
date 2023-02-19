from django.urls import path
from .views import product_list, product_detail, cart_list, cart_detail

urlpatterns = [
    path('product/', product_list),
    path('product/<int:pk>/', product_detail),
    path ('cart/', cart_list),
    path('cart/<int:pk>/', cart_detail),
]

