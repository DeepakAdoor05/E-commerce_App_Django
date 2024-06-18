from django.db import models
from django.contrib.auth.models import User
# Model for Customer.

class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=200)
    address=models.TextField()
    user=models.OneToOneField(user,on_delete=models.CASCADE,related_name='customer_profile')
    phone=models.CharField(max_length=10)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    deleted_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name