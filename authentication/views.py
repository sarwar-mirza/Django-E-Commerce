from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import SignUpUserCreationForm, LoginAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

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





