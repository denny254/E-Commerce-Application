from django.shortcuts import render
from .models import * 
from django.http import JsonResponse
import json 
import datetime 
from . utils import cookieCart, cartData, guestOrder
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def store(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    
        
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
         
    context = {'items': items, "order": order, "cartItems":cartItems }
    return render(request, 'store/cart.html', context)


def checkout(request):
  
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
        
    context = {"items":items, "order":order, "cartItems":cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body.decode('utf-8'))
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('productId:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        Customer=customer, complete=False)
    
    # Ensure OrderItem is defined before accessing it
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)
        
    order_item.save()
    
    if order_item.quantity <= 0:
        order_item.delete()
    
    return JsonResponse('Item was added', safe=False)

@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:

        customer,order=guestOrder(request,data)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()
    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shippingInfo']['address'],
            city=data['shippingInfo']['city'],
            zipcode=data['shippingInfo']['zipcode'],
        )
    return JsonResponse("Checkout is being processed", safe=False)