from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from product.validators import validate_file_size

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True) 
    stock = models.PositiveBigIntegerField()
    
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products" # models.CASCADE(delete all under that model)
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(
        upload_to="products/images/", validators=[validate_file_size])
    # for files
    # file = models.FileField(upload_to="product/files",validators=FileExtensionValidator(['pdf']))

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ratings = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.first_name} on {self.product.name}"
# Step to build API
    # Model
    # Serializer
    # Viewset
    # Router