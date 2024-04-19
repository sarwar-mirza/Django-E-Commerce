from django.urls import path
from paybill import views

urlpatterns = [
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
]
