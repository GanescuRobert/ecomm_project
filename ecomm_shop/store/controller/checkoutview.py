
import random
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from store.models import Order, OrderItem, Product, Cart

@login_required(login_url='loginpage')
def viewcheckout(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)

    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    context = {'cartitems': cartitems, 'total_price': total_price}

    return render(request, "store/checkout.html", context)

def __get_tracking_no():
    track_no = 'rnd_ec'+ str(random.randint(111111,999999))
    while Order.objects.filter(tracking_no=track_no) is None:
        track_no = 'rnd_ec'+ str(random.randint(111111,999999))
    return track_no
def __get_cart_total_price(cart):
    cart_total_price = 0
    for item in cart:
        cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
    return cart_total_price

@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == 'POST':
        neworder = Order()
        
        neworder.user = request.user 
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.zipcode = request.POST.get('zipcode')
        neworder.other = request.POST.get('other')    
        neworder.payment_mode = request.POST.get('payment_mode')
    
        cart = Cart.objects.filter(user=request.user)
        neworder.total_price = __get_cart_total_price(cart)
        
        neworder.tracking_no = __get_tracking_no()
        neworder.save()
        
        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.selling_price,
                quantity= item.product_qty,
            )
       
        orderproduct = Product.objects.filter(id=item.product_id).first()
        orderproduct.quantity -= item.product.qty
        orderproduct.save()
        

        Cart.objects.filter(user=request.user).delete()
        messages.success(request, "Your order has been placed successfully")    

    return redirect('/')