from rest_framework import serializers


class ProductItemSerializer(serializers.Serializer):
  product_id=serializers.IntegerField()
  quantity=serializers.IntegerField()


class SaleCreateSerializer(serializers.Serializer):
  customer_id=serializers.IntegerField()
  #user_id=serializers.IntegerField()
  payment_method=serializers.CharField(max_length=50)
  products=ProductItemSerializer(many=True)
  
  def validate_products(self, value):
    if not value:
      raise serializers.ValidationError('Debe haber al menos un producto')
    return value
