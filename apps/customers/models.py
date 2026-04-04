from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
  name = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  nit = models.CharField(max_length=50, unique=True)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=10)
  created_at = models.DateTimeField(auto_now_add=True)

  user = models.OneToOneField(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='customer'
  )

def __str__(self):
        return f'{self.name} {self.lastname} - {self.nit}'


