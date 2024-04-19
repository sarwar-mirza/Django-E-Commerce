from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import ProductInfo
from authentication.models import CustomerInfo

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from paybill.models import Cart
from django.db.models import Q
from django.contrib.auth.models import User
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



# Product detail
class ProductDetailView(View):
    def get(self, request, pk):
        product = ProductInfo.objects.get(pk=pk)
        
        item_already_in_cart = False      # same product select user
        item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user.id)).exists()
        return render(request, 'enroll/product_detail.html', {'product':product, 'item_already_in_cart':item_already_in_cart})



# Category for Audi & Bugatti
def audi_car(request, data=None):
    if data == None:
        audis = ProductInfo.objects.filter(category="Audi")
    elif data == 'Audi_Fuel' or data == 'Audi_Electric':
        audis = ProductInfo.objects.filter(category="Audi").filter(brand=data)
    elif data == 'Below':
        audis = ProductInfo.objects.filter(category="Audi").filter(discounted_price__lt=4200000)
    elif data == 'Above':
        audis = ProductInfo.objects.filter(category="Audi").filter(discounted_price__gt=4200000)
    return render(request, 'enroll/audi_car.html', {"audis":audis})


def bugatti_car(request, data=None):
    if data == None:
        bugattis = ProductInfo.objects.filter(category="Bugatti")
    elif data == 'Bugatti_Fuel' or data == 'Bugatti_Electric':
        bugattis = ProductInfo.objects.filter(category="Bugatti").filter(brand=data)
    elif data == 'Below':
        bugattis = ProductInfo.objects.filter(category="Bugatti").filter(discounted_price__lte=9500000)
    elif data == 'Above':
        bugattis = ProductInfo.objects.filter(category="Bugatti").filter(discounted_price__gt=9500100)
    return render(request, 'enroll/bugatti_car.html', {"bugattis":bugattis})




# Address
# @method_decorator(login_required, name='dispatch')
class AddressView(View):
     def get(self, request):
        add = CustomerInfo.objects.filter(user=request.user)
        return render(request, 'enroll/address.html', {'address':add, 'active':'btn-primary'})

