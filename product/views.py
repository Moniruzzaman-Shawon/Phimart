from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializer import ProductSerializer

# Create your views here.
@api_view() # to set response as api view
def view_specific_product(request, id):
        product = get_object_or_404(Product, pk=id)
        product = Product.objects.get(pk=id)
        serilizer = ProductSerializer(product)
        return Response(serilizer.data)
    

@api_view() 
def view_categories(request):
    return Response({"message": "Categories"})