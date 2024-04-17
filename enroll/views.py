from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ProductInfo

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'enroll/home.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        audi = ProductInfo.objects.filter(category="Audi")
        bmw = ProductInfo.objects.filter(category='BMW')
        bugatti = ProductInfo.objects.filter(category="Bugatti")
        mercedes = ProductInfo.objects.filter(category="Mercedes")
        range_rover = ProductInfo.objects.filter(category="Range Rover")
        context = {'audi':audi, 'bmw':bmw, 'bugatti':bugatti, 'mercedes':mercedes, 'range_rover':range_rover}
        return context



