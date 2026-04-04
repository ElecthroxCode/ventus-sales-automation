from django.urls import path
from .views.dashboard_views import (
  dashboard_home,
  create_sale, sales_list, 
  products_list,
  sales_detail_view, 
  customers_view, 
  customer_detail_view,
  )

urlpatterns =[
  path('', dashboard_home, name='dashboard_home'),
  path('create-sales/', create_sale, name='create_sales'),
  path('sales/', sales_list, name='sales_list'),
  path('products/', products_list, name='products_list'),
  path('sales/<int:pk>/', sales_detail_view, name='sales_detail'),
  path('customers/', customers_view, name='customers_list'),
  path('customers/<int:pk>/', customer_detail_view, name='customer_detail')
 
  
]

