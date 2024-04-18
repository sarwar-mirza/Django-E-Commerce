from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import CustomerInfo


# Sign up forms
class SignUpUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        error_messages= {'required': 'Enter your passwrod'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control", "placeholder":"Password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        error_messages= {'required': 'Enter Your confirm password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control", "placeholder":"Re-Enter Password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        error_messages = {
            'username': {'required': 'Enter your username'},
            'first_name': {'required': 'Enter Your first name'},
            'last_name': {'required': 'Enter your last name'},
            'email': {'required': 'Enter your email'},
        }
        
        labels = {
            'email': 'Email',
        }
        
        widgets = {
            'username': forms.TextInput(attrs={"class":"form-control", "placeholder":"Username"}),
            'first_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}),
            'last_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}),
            'email': forms.EmailInput(attrs={"class":"form-control", "placeholder":"@gmail.com"}),
        }






# Create Login page
class LoginAuthenticationForm(AuthenticationForm):
    username = UsernameField(error_messages={'required':'Enter Your Username'}, widget=forms.TextInput(attrs={"autofocus": True, "class":"form-control", "placeholder":"Username"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        error_messages= {'required':'Enter your passoword'},
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class":"form-control", "placeholder":"Password"}),
    )



# Profile 
class ProfileCustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        # ordering field
        fields = ['first_name', 'last_name', 'division', 'city', 'zipcode', 'area']
        
        # lable
        labels = { 
            'zipcode': 'Post Code'
        }
        
        error_messages = {
            'first_name': {'required': 'Enter Your First Name'},
            'last_name': {'required': 'Enter Your Last Name'},
            'division': {'required': 'Enter Your division'},
            'city': {'required': 'Enter Your city'},
            'zipcode': {'required': 'Enter Your Post Code'},
            'area': {'required': 'Enter Your Area'},
        }
        
        
        # widgets
        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}),
            'last_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}),
            'division': forms.Select(attrs={"class":"form-control", "placeholder":"Division"}),
            'city': forms.TextInput(attrs={"class":"form-control", "placeholder":"City"}),
            'zipcode': forms.TextInput(attrs={"class":"form-control", "placeholder":"zipcode"}),
            'area': forms.TextInput(attrs={"class":"form-control", "placeholder":"Village, House No, Road No "}),
        }



