from  django.urls import path
from authentication import views


urlpatterns = [
    path('signup/', views.SignUpTemplateView.as_view(), name='signup-page'),
]
