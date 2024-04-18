from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import SignUpUserCreationForm, LoginAuthenticationForm, ProfileCustomerInfoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import CustomerInfo

# Create your sign up views here.
class SignUpTemplateView(TemplateView):
    template_name = 'authentication/signup.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = SignUpUserCreationForm()
        context = {'form': fm}
        return context
    
    
    def post(self, request):       # post request
        fm = SignUpUserCreationForm(request.POST)
        
        if fm.is_valid():
            fm.save()
            
            # message framework
            messages.success(request, 'Congratulations! Your account has been created. ')
            fm = SignUpUserCreationForm()       # After submission form will show blank
        return render(request, 'authentication/signup.html', {'form':fm})




# Create Login Function based view
def loginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginAuthenticationForm(request=request, data = request.POST)
            
            if fm.is_valid():
                un = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']
                
                user = authenticate(username=un, password=pw)
                
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/accounts/profile/')
        else:
            fm = LoginAuthenticationForm()
        return render(request, 'authentication/login.html', {'form':fm})
    
    else:
        return HttpResponseRedirect('/accounts/profile/')




# Profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ProfileCustomerInfoForm(request.POST, instance=request.user)
            
            if fm.is_valid():
                usr = request.user
                f_name = fm.cleaned_data['first_name']
                l_name = fm.cleaned_data['last_name']
                divi= fm.cleaned_data['division']
                ct= fm.cleaned_data['city']
                zp= fm.cleaned_data['zipcode']
                ar= fm.cleaned_data['area']
                
                reg = CustomerInfo(user=usr, first_name=f_name, last_name=l_name, division=divi, city=ct, zipcode=zp, area=ar)
                reg.save()
                
                messages.success(request, 'Congratulations! profile updated successfully.')
        else:
            fm = ProfileCustomerInfoForm(instance=request.user)
        return render(request, 'authentication/profile.html', {'form':fm, 'active':'btn-primary'})
    
    else:
        return HttpResponseRedirect('/accounts/login/')






