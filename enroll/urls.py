from django.urls import path
from enroll import views

urlpatterns = [
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail_page"),
    
    path('audi/', views.audi_car, name='audiPage'),
    path('audi/<slug:data>', views.audi_car, name='audiPageData'),
    
    path('bugatti/', views.bugatti_car, name='bugattiPage'),
    path('bugatti/<slug:data>', views.bugatti_car, name='bugattiPageData'),
    
    
]


