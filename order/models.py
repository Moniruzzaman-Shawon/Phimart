from django.db import models
from users.models import User
from product.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,related_name='cart'

    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    