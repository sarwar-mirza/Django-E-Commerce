from  django.urls import path
from authentication import views


urlpatterns = [
    path('signup/', views.SignUpTemplateView.as_view(), name='signup-page'),
    path('login/', views.loginView, name='login-page'),
    path('profile/', views.user_profile, name='profile-page'),
    path('logout/', views.user_logout, name='logout-page'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password-page'),
    path('change-password-done/', views.ChangePasswordDoneView.as_view(), name='change-password-done-page'),
]
