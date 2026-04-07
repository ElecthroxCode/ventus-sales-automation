from django.urls import path
from .views import CustomerCreateView, CustomerListView, CustomerDetailView


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'), 
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    

]