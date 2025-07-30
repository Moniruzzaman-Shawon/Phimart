from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializer import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.generics import ListCreateAPIView


# Create your views here.
# @api_view(['GET', 'POST'])
# def view_products(request):
#     if request.method== 'GET':
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data) # deserializer (to add new data)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.validated_data)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class ViewProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data) # deserializer (to add new data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductList(ListCreateAPIView): # View products
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    # def get_queryset(self):
    #     return Product.objects.select_related('category').all()
    
    # def get_serializer_class(self):
    #     return ProductSerializer 
    
    # def get_serializer_context(self):   # to use hyperlink 
    #     return {'Request': self.request}
    


@api_view() # to set response as api view
def view_specific_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product = Product.objects.get(pk=id)
    serilizer = ProductSerializer(product)
    return Response(serilizer.data)


class ViewSpecificProduct(APIView):
    def get(self, request,id):
        product = get_object_or_404(Product, pk=id)
        serilizer = ProductSerializer(product)
        return Response(serilizer.data)
    
    def put(self,request):
        product = Product.objects.get(pk=id)
        serilizer = ProductSerializer(product,data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.data)

# @api_view() 
# def view_categories(request):
#     categories = Category.objects.annotate(product_count = Count('products')).all()
#     serializer = CategorySerializer(categories, many= True)
#     return Response(serializer.data)

class ViewCategories(APIView):
    def get(Self, request):
        categories = Category.objects.annotate(product_count = Count('products')).all()
        serializer = CategorySerializer(categories, many= True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer

# class ViewSpecificCategory(APIView):
#     def get(self, request, id):
#         category = get_object_or_404(Category.objects.annotate(product_count = Count('products')).all(), pk = id)
#         serilizer = CategorySerializer(category)
#         return Response(serilizer.data, status=status.HTTP_201_CREATED)

#     def put(self, request, id):
#         category = get_object_or_404(Category.objects.annotate(product_count = Count('products')).all(), pk = id)
#         serializer = CategorySerializer(category,data = request.data)
#         serializer.save()
#         return ResourceWarning(serializer.data)
    
#     def delete():
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view()
# def view_specific_category(request, pk):
#     category = get_object_or_404(
#         Category.objects.annotate(product_count = Count('products')).all(), 
#         pk = id)
#     serilizer = CategorySerializer(category)
#     return Response(serilizer.data, status=status.HTTP_201_CREATED)