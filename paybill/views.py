from django.shortcuts import render, redirect
from enroll.models import ProductInfo
from .models import Cart
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = ProductInfo.objects.get(id=product_id)

 Cart(user=user, product=product).save()

 return redirect('/cart')


@login_required
def show_cart(request):
 if request.user.is_authenticated:
  user = request.user
  cart = Cart.objects.filter(user=user)

  amount = 0.0
  shipping_amount = 30000.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user == user]

  if cart_product:
   for p in cart_product:
    tempamount = (p.quantity  *  p.product.discounted_price)
    amount += tempamount
    totalamount = amount + shipping_amount
   return render(request, 'paybill/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
  else:
   return render(request, 'paybill/emptycart.html', {'totalitem':totalitem})



