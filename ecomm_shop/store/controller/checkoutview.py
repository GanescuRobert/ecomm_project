
from functools import total_ordering
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from store.models import Order, OrderItem, Product, Cart, Profile
from django.contrib import messages


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

    userprofile = Profile.objects.filter(user=request.user).first()
    context = {'cartitems': cartitems,
               'total_price': total_price, "userprofile": userprofile}

    return render(request, "store/checkout.html", context)


def __get_tracking_no():
    track_no = 'rnd_ec' + str(random.randint(111111, 999999))
    while Order.objects.filter(tracking_no=track_no) is None:
        track_no = 'rnd_ec' + str(random.randint(111111, 999999))
    return track_no


def __get_cart_total_price(cart):
    cart_total_price = 0
    for item in cart:
        cart_total_price = cart_total_price + \
            item.product.selling_price * item.product_qty
    return cart_total_price


@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == 'POST':
        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()
        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.zipcode = request.POST.get('zipcode')
            userprofile.details = request.POST.get('other')
            userprofile.save()

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
        neworder.details = request.POST.get('other')

        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')

        cart = Cart.objects.filter(user=request.user)
        neworder.total_price = __get_cart_total_price(cart)

        neworder.tracking_no = __get_tracking_no()
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty,
            )

        orderproduct = Product.objects.filter(id=item.product_id).first()
        orderproduct.quantity -= item.product.quantity
        orderproduct.save()

        Cart.objects.filter(user=request.user).delete()

        pay_mode = request.POST.get('payment_mode')
        if pay_mode == "Paid by Razorpay":
            return JsonResponse({"status": "Your order has been placed successfully"})
        else:
            messages.success(
                request, "Your order has been placed successfully")

    return redirect('/')


@login_required(login_url='loginpage')
def razorpaycheck(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.selling_price * item.product_qty

    return JsonResponse({
        'total_price': total_price
    })


def orders(request):
    return HttpResponse("My orders page")
