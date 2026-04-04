from django.urls import path
from .views import CustomerCreateView, CustomerSearchView, CustomerListView, CustomerDetailView


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'), 
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('search/', CustomerSearchView.as_view(), name='customer_search'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    

]