from rest_framework import serializers
from apps.sales.models import Sale, SaleDetail


class SaleDetailSerializer(serializers.ModelSerializer):
  product_name = serializers.CharField(source = 'product.name', read_only = True)
  class Meta:
    model = SaleDetail
    fields = ['product', 'product_name', 'quantity', 'unit_price', 'subtotal']

class SaleListSerializer(serializers.ModelSerializer):
  details = SaleDetailSerializer(many=True)
  
  customer_name = serializers.SerializerMethodField()

  date = serializers.DateTimeField(format="%Y-%m-%d")

  class Meta:
    model = Sale
    fields = [
      'id',
      'customer',
      'customer_name',
      'total',
      'payment_method',
      'date',
      'details'
    ]

  def get_customer_name(self, obj):
    return f"{obj.customer.name} {obj.customer.lastname}"



