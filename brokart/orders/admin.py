from django.contrib import admin
from .models import Orders,Ordered_Item
# Register your models here.
# This the class which helps us to customize the default admin given by Orders app
class OrderAdmin(admin.ModelAdmin):
    list_filter=[
        "owner",
        "order_status",
    ]
    search_fields=(
        "owner",
        "id"
    )

admin.site.register(Orders,OrderAdmin)