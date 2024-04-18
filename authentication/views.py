from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SignUpUserCreationForm
from django.contrib import messages

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





