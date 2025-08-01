from rest_framework import serializers
from decimal import Decimal
from product.models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']    

    product_count = serializers.IntegerField(read_only=True)

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source = 'price') #source for identify, now I can change 'price_name'

#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     # category = serializers.PrimaryKeyRelatedField(
#     #     queryset = Category.objects.all()
#     # )
#     # category = serializers.StringRelatedField()
#     # category = CategorySerializer()
#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),
#         view_name =  'view-specific-category'
#     )

#     def calculate_tax(self,product):
#         return round(product.price * Decimal(1.1), 2)
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # ---- fields = '__all__' # to show all fields (but not recommended)
        fields = ["id", "name", 'description', 'price', 'stock', 'category', 'price_with_tax']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.HyperlinkedRelatedField(
    # queryset = Category.objects.all(),
    #     view_name =  'view-specific-category')
    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1) , 2)
    
    def validate_price(self,price):
        if price < 0:
            raise serializers.ValidationError('Price could not be negative')
        return price

    # def validate(self, attrs):
    #     if attrs['password1'] != attrs['password2']:
    #         raise serializers.ValidationError("Password does not match")


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'ratings' , 'comment']
        read_only_fields = ['user', 'product']

    def create(self, validated_data):
        product_id = self.context[ 'product_id']
        review = Review.objects.create(product_id=product_id, **validated_data)
        return review