from django.db import models
from django.contrib.auth.models import User
from apps.customers.models import Customer
from apps.products.models import Product

# Create your models here.

class Sale(models.Model):
  date = models.DateTimeField(auto_now_add=True)
  total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  
  PAYMENT_METHOD_CHOICES = [
    ('cash', 'Efectivo'),
    ('card', 'Tarjeta'),
    ('transfer', 'Transferencia'),
  ]

  payment_method = models.CharField(
    max_length=20,
    choices=PAYMENT_METHOD_CHOICES
  )

#sales N --------- 1 Customer
  customer = models.ForeignKey(
    Customer,
    on_delete=models.CASCADE,
    related_name='sales'
  )
#sales N -------------- 1 User
  user = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='sales'
  )

  def __str__(self):
    return f'Sale id: {self.id}'
  

#model SaleDetail
class SaleDetail(models.Model):
  quantity = models.IntegerField()
  unit_price = models.DecimalField(max_digits=10, decimal_places=2)
  subtotal = models.DecimalField(max_digits=10, decimal_places=2)
  
  sale = models.ForeignKey(
    Sale,
    on_delete=models.CASCADE,
    related_name='details'
  )

  product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name='sale_details'
  )

  def __str__(self):
    return f'{self.unit_price} x {self.quantity}'
