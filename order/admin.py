from django.contrib import admin
from order.models import Cart, CartItem
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display =['id', 'user']


try:
    admin.site.register(Cart, CartAdmin)
except AlreadyRegistered:
    pass
admin.site.register(CartItem)
