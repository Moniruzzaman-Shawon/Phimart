from django.contrib import admin
from order.models import Cart, CartItem, Order, OrderItem
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display =['id', 'user']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id', 'user', 'status']


try:
    admin.site.register(Cart, CartAdmin)
except AlreadyRegistered:
    pass
admin.site.register(CartItem)
admin.site.register(OrderItem)
