from django.db import models
from customers.models import Customer
from products.models import Product
# Model for orders.

# Data Model for order.
class Orders(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    # Stages of order.
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_DELIVERED,"ORDER_DELIVERED"),
                   (ORDER_REJECTED,"ORDER_REJECTED")
                   )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='owner',null=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    deleted_at=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return "order-{}-{}".format(self.id,self.owner.user.username)
    
# Model for ordered item.
class Ordered_Item(models.Model):
    product=models.ForeignKey(Product,related_name='addaed_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Orders,related_name='added_items',on_delete=models.CASCADE)