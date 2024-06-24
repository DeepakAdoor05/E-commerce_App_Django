from django.shortcuts import render,redirect
from . models import Orders,Ordered_Item
from products.models import product
# Create your views here.

def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Orders.objects.get_or_create(
        owner=customer,
        order_status=Orders.CART_STAGE
    )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Orders.objects.get_or_create(
            owner=customer,
            order_status=Orders.CART_STAGE
        )
        print(cart_obj)
        product_obj=product.objects.get(pk=product_id)
        ordered_item=Ordered_Item.objects.create(
            product=product_obj,
            owner=cart_obj,
            quantity=quantity
        )
        
    return redirect('cart')