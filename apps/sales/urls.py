from django.urls import path
from .views import SaleCreateView, SalesListView, SaleDetailView, PaymentMethodListView


urlpatterns=[
  path('create/', SaleCreateView.as_view(), name='create_sale'),
  path('', SalesListView.as_view(), name='list_sales'),
  path('<int:pk>/', SaleDetailView.as_view(), name='detail_sale'),
  path('payment-methods/', PaymentMethodListView.as_view()),
]



