from django.urls import path
from paybill import views

urlpatterns = [
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    
    # Quantity plus, minus, remove
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    
    path('checkout/',  views.checkout, name='checkout'),
]
