from django.urls import path
from enroll import views

urlpatterns = [
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail_page"),
]


