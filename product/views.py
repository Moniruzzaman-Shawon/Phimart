from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializer import ProductSerializer, CategorySerializer
from django.db.models import Count

# Create your views here.
@api_view(['GET', 'POST'])
def view_products(request):
    if request.method== 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data) # deserializer (to add new data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view() # to set response as api view
def view_specific_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product = Product.objects.get(pk=id)
    serilizer = ProductSerializer(product)
    return Response(serilizer.data)


@api_view() 
def view_categories(request):
    categories = Category.objects.annotate(product_count = Count('products')).all()
    serializer = CategorySerializer(categories, many= True)
    return Response(serializer.data)


@api_view()
def view_specific_category(request, pk):
    category = get_object_or_404(Category, pk = pk)
    serilizer = CategorySerializer(category)
    return Response(serilizer.data)