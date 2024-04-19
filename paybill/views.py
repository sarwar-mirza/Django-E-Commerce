from django.shortcuts import render, redirect
from enroll.models import ProductInfo
from .models import Cart, OrderPlaced
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.http import JsonResponse

from authentication.models import CustomerInfo
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
 totalitem = 0
 if request.user.is_authenticated:
   totalitem = len(Cart.objects.filter(user=request.user))
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



# Quantity plus, minus, remove

def plus_cart(request):                     # Plus Quantity
 if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()

    amount = 0.0
    shipping_amount = 30000.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]

    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
      #totalamount = amount + shipping_amount

    data = {
      'quantity': c.quantity,
      'amount': amount,
      'totalamount': amount + shipping_amount
    }

    return JsonResponse(data)
 

def minus_cart(request):                                      # minus Quantity
 if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity -= 1
    c.save()

    amount = 0.0
    shipping_amount = 30000.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]

    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
      

    data = {
      'quantity': c.quantity,
      'amount': amount,
      'totalamount': amount + shipping_amount
    }

    return JsonResponse(data)
 


def remove_cart(request):                     # Remove Quantity
 if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    
    c.delete()

    amount = 0.0
    shipping_amount = 30000.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]

    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
      

    data = {
      'amount': amount,
      'totalamount': amount + shipping_amount
    }

    return JsonResponse(data)



@login_required
def checkout(request):
 totalitem = 0
 user = request.user
 add = CustomerInfo.objects.filter(user=user)
 cart_items = Cart.objects.filter(user=user)

 amount = 0.0
 shipping_amount = 70.0
 totalamount = 0.0

 cart_product = [p for p in Cart.objects.all() if p.user == request.user]

 if cart_product:
  for p in cart_product:
   tempamount = (p.quantity * p.product.discounted_price)
   amount += tempamount
  totalamount = amount + shipping_amount

 if request.user.is_authenticated:
   totalitem = len(Cart.objects.filter(user=request.user))


 return render(request, 'paybill/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items': cart_items, 'totalitem':totalitem})




# check out peyment done
@login_required
def payment_done(request):
 user = request.user
 custid = request.GET.get('custid')
 customer = CustomerInfo.objects.get(id=custid)
 cart_items = Cart.objects.filter(user=user)

 for c in cart_items:
  OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
  c.delete()
 return redirect("orders")


# Order Placed
@login_required
def orders(request):
 op = OrderPlaced.objects.filter(user=request.user)
 return render(request, 'paybill/orders.html', {'order_placed':op})

